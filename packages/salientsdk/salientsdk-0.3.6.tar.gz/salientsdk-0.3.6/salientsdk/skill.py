#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Skill and validation."""

import numpy as np
import pandas as pd
import xarray as xr


def crpss(
    forecast: xr.Dataset | xr.DataArray,
    reference: xr.Dataset | xr.DataArray,
) -> xr.Dataset | xr.DataArray:
    """Continuous Ranked Probability Skill Score.

    CRPSS measures the relative skill improvement of one CRPS forecast over another.
    Positive values can roughly interpreted as percentages, so a CRPSS of 0.10 means a 10% improvement.
    Zero values mean no improvement, and negative values mean the forecast is worse than the reference.

    Args:
        forecast: The forecast data
        reference: The reference baseline data

    Returns:
        xr.DataArray: The CRPSS result
    """
    skill_score = 1 - (forecast / reference)

    skill_score = _set_array_name(skill_score, "crpss")

    return skill_score


def crps(
    observations: xr.Dataset | xr.DataArray | str,
    forecasts: xr.Dataset | xr.DataArray | str | list[str] | pd.DataFrame,
    qnt_dim: str = "quantiles",
) -> xr.DataArray:
    """Calculate Continuous Ranked Probability Score.

    CRPS is used to calculate the skill of a probabilistic forecast.
    CRPS is defined as 2 times the integral of the quantile loss over the distribution.
    Zero CRPS indicates a perfect forecast.

    Args:
        observations: `DataArray` of observed values, aka "truth", or a `nc` filename.
            `observations` should usually have the same coordinates as `forecasts`.
            If `observations` has a `daily` timescale to match
            a `weekly`, `monthly`, or `quarterly` timescale for `forecasts.`
        forecasts: `DataArray` of forecasted values.  May also be:
          * a file reference to a `nc` file
          * a vector of file references to `nc` files
          * a DataFrame with a `file_name` column
        qnt_dim: Name of the quantile dimension in the forecast array.
            Defaults to `quantiles`, which is the dimension name returned by
            `forecast_timeseries`.

    Returns:
        xr.DataArray: The CRPS of the `forecasts` quantiles vs. the `observations`.

    """
    return _calc_skill(observations, forecasts, skill_func=_crps_core, qnt_dim=qnt_dim)


def _crps_core(
    observations: xr.Dataset | xr.DataArray,
    forecasts: xr.Dataset | xr.DataArray,
    qnt_dim="quantiles",
) -> xr.Dataset | xr.DataArray:
    """The fundamental Continuous Ranked Probability Score calculation.

    This function differs from the user-visible `crps` function in that it does not
    perform any vectorization, coordinate alignment, or validation.
    """
    diff = observations - forecasts
    qnt_val = diff[qnt_dim]

    qnt_score = 2 * np.maximum(qnt_val * diff, (qnt_val - 1) * diff)
    skill = qnt_score.integrate(coord=qnt_dim)
    skill.attrs = forecasts.attrs.copy()

    skill = _set_array_name(skill, "crps")

    return skill


def _calc_skill(
    observations: xr.Dataset | xr.DataArray | str,
    forecasts: xr.Dataset | xr.DataArray | str | list[str] | pd.DataFrame,
    skill_func: callable,
    **kwargs,
) -> xr.DataArray:
    """Calculate a skill score.

    Handles vectorization and coordinate alignment for skill functions.  Skill itself
    is calculated by the `skill_func` function.

    Args:
        observations: `DataArray` or `Dataset` of observed ("truth") values , or a `nc` filename.
            `observations` should usually have the same coordinates as `forecasts`.
            If `observations` has a `daily` timescale, the system will aggregate match
            a `weekly`, `monthly`, or `quarterly` timescale for `forecasts.`
        forecasts: `Dataset` or `DataArray` of forecasted values.  May also be:
          * a file reference to a `nc` file
          * a vector of file references to `nc` files, which will calculate skill for
            each file and return the average across all forecasts.
          * a DataFrame with a `file_name` column
        skill_func: The skill function to use.
        **kwargs: Additional arguments to pass to `skill_func`.

    Returns:
        xr.DataArray: The skill of the `forecast` values vs. the `observation`s.

    """

    def extract_df_files(obj, col_name="file_name"):
        """Extract file names from a DataFrame, if passed in."""
        if isinstance(obj, pd.DataFrame):
            assert col_name in forecasts.columns, f"DataFrame must have a '{col_name}' column."
            obj = obj[col_name].tolist()
        return obj

    if observations is None or observations is pd.NA:
        return None
    elif isinstance(observations, str):
        observations = xr.load_dataset(observations)
    elif not isinstance(observations, xr.DataArray) and not isinstance(observations, xr.Dataset):
        raise ValueError(
            f"observations {type(observations)} must be Dataset, DataArray, or filename"
        )

    forecasts = extract_df_files(forecasts)
    if forecasts is None or forecasts is pd.NA:
        return None
    elif isinstance(forecasts, str):
        # We want to load_datasaet instead of load_dataarray in order to preserve forecast_period
        forecasts = xr.load_dataset(forecasts)
    elif isinstance(forecasts, list):
        skill = [_calc_skill(observations, fcst, skill_func, **kwargs) for fcst in forecasts]
        skill = [s for s in skill if s is not None]
        if len(skill) == 0:
            return None
        elif len(skill) == 1:
            return skill[0]

        # What if forecast=all and there are multiple forecast dates?
        concat_dim = _find_coord(skill[0], "forecast_date", strict=True)
        skill = xr.concat(skill, dim=concat_dim)

        skill = skill.mean(dim=concat_dim, keep_attrs=True)

        return skill
    elif not isinstance(forecasts, xr.DataArray) and not isinstance(forecasts, xr.Dataset):
        raise ValueError(
            f"forecast {type(forecasts)} must be a Dataset, DataArray, DataFrame[file_name], or filename."
        )

    # At this point, all vectorization and file loading should be done.  Now we need to make sure
    # that the coordinates match.
    if "time" in observations.coords:
        lead_dim = _find_coord(forecasts, "lead_", strict=False)
        if lead_dim is not None:
            observations = align_daily_obs_to_lead(observations, forecasts, lead_dim[5:])
        elif "time" in forecasts.coords:
            (observations, forecasts) = _align_time_to_lead(observations, forecasts)

    return skill_func(observations, forecasts, **kwargs)


def _set_array_name(ds: xr.Dataset | xr.DataArray, name: str) -> xr.Dataset | xr.DataArray:
    """Set the name of the data array or first dataset variable."""
    if isinstance(ds, xr.DataArray):
        ds.name = name
    elif isinstance(ds, xr.Dataset):
        if len(ds.data_vars) == 1:
            ds = ds.rename_vars({list(ds.data_vars)[0]: name})

    ds.attrs["short_name"] = name
    ds.attrs["long_name"] = (
        ds.attrs["long_name"] + " " if "long_name" in ds.attrs else ""
    ) + name.upper()

    return ds


def _extract_array_name(ds: xr.Dataset | xr.DataArray) -> str:
    """Extract the name of the first data variable in a dataset."""
    if isinstance(ds, xr.Dataset):
        # get the string name of the first forecast data var:
        return next(iter(ds.data_vars))
    elif isinstance(ds, xr.DataArray):
        return ds.name
    else:
        raise ValueError(f"Must be a Dataset or DataArray, not {type(ds)}")


def align_daily_obs_to_lead(
    observations: xr.Dataset | xr.DataArray,
    forecasts: xr.Dataset | xr.DataArray,
    timescale: str,
) -> xr.Dataset | xr.DataArray:
    """Convert daily observations to match forecasts denominated by a coarse lead time.

    Args:
        observations: Daily observed values with coordinate `time`.
        forecasts: The forecasted values with coordinate `lead_<timescale>` and
          `forecast_period_<timescale>`.
        timescale: The forecast period of the forecast, corresponding to data variables
            `lead_<timescale>` and `forecast_period_<timescale>`.
            Will typically be `weekly`, `monthly`, or `quarterly`.

    Returns:
        xr.Dataset | xr.DataArray: An aggregated version of `observations` with coordinate
            `lead_<timescale>` instead of `time`.
    """
    lead_name = f"lead_{timescale}"
    data_name = _extract_array_name(forecasts)
    period_name = f"forecast_period_{timescale}"

    lead_vals = forecasts[lead_name].values

    # groupby_bins creates bins that are right-inclusive, so we start the
    # binning one day early:
    first_day = forecasts[period_name].isel(nbnds=0)[0] - np.timedelta64(1, "D")
    bins = np.append(first_day, forecasts[period_name].isel(nbnds=1))

    observations = (
        observations.groupby_bins("time", bins)
        .mean()
        .assign_coords(lead=("time_bins", lead_vals))
        .rename({"lead": lead_name})
        .swap_dims({"time_bins": lead_name})
        .drop_vars("time_bins")
    )

    if isinstance(observations, xr.Dataset):
        obs_name = _extract_array_name(observations)
        observations = observations.rename({obs_name: data_name})
    elif isinstance(observations, xr.DataArray):
        observations.name = data_name

    return observations


def _find_coord(
    ds: xr.DataArray | xr.Dataset, starts_with: str, strict: bool = True
) -> str | None:
    """Find a coordinate that starts with a given string.

    Args:
        ds: The dataset or dataarray to search
        starts_with: Search for coordinates that begin with this string
        strict: If True, raise an error if no match is found.

    Returns:
        str: The name of the coordinate that starts with `starts_with`
            or `None` if no coordinate was found
    """
    found = next((coord for coord in ds.coords if coord.startswith(starts_with)), None)
    if strict:
        assert found is not None, f"No {starts_with} coordinate found."
    return found


def _align_time_to_lead(
    observations: xr.DataArray, forecasts: xr.DataArray
) -> (xr.DataArray, xr.DataArray):
    """Align or aggregate observations to match the granularity of forecasts.

    Args:
        observations (xr.DataArray): The observed values with coordinate `time`.
        forecasts (xr.DataArray): The forecasted values with coordinate `time`.

    Returns:
        tuple: Aligned or aggregated observations and forecasts with updated 'lead' coordinates.
    """
    # Convert time coordinates to pd.DatetimeIndex and infer frequencies

    # obs_time = _ensure_freq(observations.time.values)
    fcst_time = _ensure_freq(forecasts.time.values)

    lead_times = range(1, len(forecasts.time) + 1)
    forecasts = forecasts.assign_coords(lead=("time", lead_times))

    # TODO: trim observations to match forecast time range for efficiency.
    observations = observations.resample(time=fcst_time.freq).mean()

    observations, forecasts = xr.align(observations, forecasts, join="inner")
    observations = observations.assign_coords(lead=("time", forecasts.lead.values))

    forecasts = forecasts.swap_dims({"time": "lead"})
    observations = observations.swap_dims({"time": "lead"})

    return observations, forecasts


def _ensure_freq(time) -> pd.DatetimeIndex:
    """Ensure that a time vector has a 'freq' attribute for resampling."""
    if not isinstance(time, pd.DatetimeIndex):
        time = pd.to_datetime(time)

    if time.freq is not None:
        # Frequency is already set
        return time
    elif len(time) < 2:
        # Not enough data to infer or calculate frequency
        raise ValueError("Not enough data points to determine frequency.")
    elif len(time) == 2:
        # Manually calculate frequency from two dates.
        step = time[1] - time[0]
        days = step.days
        if days == 1:
            freq = "D"
        elif days == 7:
            day_of_week = time[0].day_name()
            freq = f"W-{day_of_week[:3].upper()}"
        elif 28 <= days <= 31:
            freq = "MS"  # ms= momth start
        elif 89 <= days <= 92:
            # Get the month for the first date
            month_of_year = time[0].month
            # Map month to the corresponding quarter start
            if month_of_year in [1, 2, 3]:
                freq = "Q-JAN"
            elif month_of_year in [4, 5, 6]:
                freq = "Q-APR"
            elif month_of_year in [7, 8, 9]:
                freq = "Q-JUL"
            elif month_of_year in [10, 11, 12]:
                freq = "Q-OCT"
        else:
            raise ValueError(f"Unknown time step: {days} days.")
    else:
        # Infer frequency from three or more dates
        freq = pd.infer_freq(time)
        if freq is None:
            raise ValueError("Unable to infer frequency from data.")

    return pd.DatetimeIndex(time, freq=freq)
