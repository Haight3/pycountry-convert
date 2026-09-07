"""
Country Name Formatting
=======================
*Created on 2026-09-06 by Isbert*
*Copyright (C) 2026 Haight Labs (https://www.haight.ai)*
*Copyright (C) 2018 TUNE, Inc. (http://www.tune.com)*
*For COPYING and LICENSE details, please refer to the LICENSE file*

This module defines the supported country-name formats and provides the
formatting operation shared by country conversion and mapping functions.
"""

COUNTRY_NAME_FORMAT_DEFAULT = "default"
COUNTRY_NAME_FORMAT_UPPER = "upper"
COUNTRY_NAME_FORMAT_LOWER = "lower"

COUNTRY_NAME_FORMATS = [COUNTRY_NAME_FORMAT_DEFAULT, COUNTRY_NAME_FORMAT_UPPER, COUNTRY_NAME_FORMAT_LOWER]


def country_name_format(cn_name: str, cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> str:
    """Format a country name using the requested letter case.

    Parameters
    ----------
    cn_name : str
        Country name to format.
    cn_name_format : str, default="default"
        Output format. Supported values are ``"default"``, ``"lower"``, and
        ``"upper"``. Other values leave the name unchanged.

    Returns
    -------
    str
        The country name in the requested format.
    """
    if cn_name_format == COUNTRY_NAME_FORMAT_DEFAULT:
        pass
    elif cn_name_format == COUNTRY_NAME_FORMAT_LOWER:
        cn_name = cn_name.lower()
    elif cn_name_format == COUNTRY_NAME_FORMAT_UPPER:
        cn_name = cn_name.upper()

    return cn_name
