"""
Continent Name Conversion
=========================
*Created on 2026-09-06 by Isbert*
*Copyright (C) 2018 TUNE, Inc. (http://www.tune.com)*
*For COPYING and LICENSE details, please refer to the LICENSE file*

This module defines continent names and converts two-letter continent codes
to their corresponding display names.
"""

CONTINENT_CODE_TO_CONTINENT_NAME = {
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "SA": "South America",
    "AF": "Africa",
    "OC": "Oceania",
    "AN": "Antarctica",
}


def convert_continent_code_to_continent_name(continent_2_code: str) -> str:
    """Convert a two-letter continent code to its continent name.

    Parameters
    ----------
    continent_2_code : str
        Two-letter continent code to convert.

    Returns
    -------
    str
        The corresponding continent name.

    Raises
    ------
    KeyError
        If the continent code is missing, is not two characters long, or is
        not recognized.
    """
    if continent_2_code is None or len(continent_2_code) != 2:
        raise KeyError(f"Invalid Continent code: '{continent_2_code}'")

    if continent_2_code not in CONTINENT_CODE_TO_CONTINENT_NAME:
        raise KeyError(f"Invalid Continent code: '{continent_2_code}'")

    return CONTINENT_CODE_TO_CONTINENT_NAME[continent_2_code]
