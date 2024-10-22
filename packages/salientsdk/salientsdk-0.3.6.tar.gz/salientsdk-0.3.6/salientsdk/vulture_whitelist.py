#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Whitelist file for vulture.

We use the vulture tool to make sure that we don't have dead code
hanging around. Sometimes vulture falsely flags a function as unused.
In that case, we add the function to this whitelist file so they are
explicitly registered as used.
"""

# from .upload_file_api import user_files
# assert user_files  # unused function (salientsdk/upload_file_api.py:220)

from .solar import _downscale_solar

assert _downscale_solar  # currently under development and skipped in testing
