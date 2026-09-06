"""
Country Code Conversion
=======================
*Created on 2026-09-06 by Isbert*
*Copyright (C) 2018 TUNE, Inc. (http://www.tune.com)*
*For COPYING and LICENSE details, please refer to the LICENSE file*

This module provides public conversions among country names and ISO 3166-1
alpha-2 and alpha-3 country codes.
"""

from .country_mappings import (
    list_country_alpha2,
    map_country_name_to_country_alpha2,
    map_country_name_to_country_alpha3,
)
from .country_name_format import (
    COUNTRY_NAME_FORMAT_DEFAULT,
    country_name_format,
)


def country_alpha2_to_country_name(
    country_2_code: str,
    cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT,
) -> str:
    """Convert an ISO 3166-1 alpha-2 code to a country name.

    Parameters
    ----------
    country_2_code : str
        Two-letter country code to convert.
    cn_name_format : str, default="default"
        Letter-case format to apply to the returned country name.

    Returns
    -------
    str
        The country name in the requested format.

    Raises
    ------
    KeyError
        If the country code is missing, is not two characters long, or is not
        recognized.
    """
    if country_2_code is None or len(country_2_code) != 2:
        raise KeyError(f"Invalid Country Alpha-2 code: '{country_2_code}'")

    from .country_mappings import map_country_alpha2_to_country_name

    dict_country_alpha2_to_country_name = map_country_alpha2_to_country_name(cn_name_format)

    if country_2_code not in dict_country_alpha2_to_country_name:
        raise KeyError(f"Invalid Country Alpha-2 code: '{country_2_code}'")

    return dict_country_alpha2_to_country_name[country_2_code]


def country_alpha3_to_country_alpha2(country_3_code: str) -> str:
    """Convert an ISO 3166-1 alpha-3 code to an alpha-2 code.

    Parameters
    ----------
    country_3_code : str
        Three-letter country code to convert.

    Returns
    -------
    str
        The corresponding two-letter country code.

    Raises
    ------
    KeyError
        If the country code is missing, is not three characters long, or is
        not recognized.
    """
    if country_3_code is None or len(country_3_code) != 3:
        raise KeyError(f"Invalid Country Alpha-3 code: '{country_3_code}'")

    from .country_mappings import map_country_alpha3_to_country_alpha2

    dict_country_alpha3_to_country_alpha2 = map_country_alpha3_to_country_alpha2()

    if country_3_code not in dict_country_alpha3_to_country_alpha2:
        raise KeyError(f"Invalid Country Alpha-3 code: '{country_3_code}'")

    return dict_country_alpha3_to_country_alpha2[country_3_code]


def country_name_to_country_alpha2(
    cn_name: str,
    cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT,
) -> str:
    """Convert a country name or code to an ISO 3166-1 alpha-2 code.

    Parameters
    ----------
    cn_name : str
        Country name, alpha-2 code, or alpha-3 code to resolve.
    cn_name_format : str, default="default"
        Letter-case format used when matching country names.

    Returns
    -------
    str
        The corresponding two-letter country code.

    Raises
    ------
    KeyError
        If the country name or code is missing or is not recognized.
    """
    if cn_name is None:
        raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

    cn_name = country_name_format(cn_name, cn_name_format)
    dict_country_name_to_country_alpha2 = map_country_name_to_country_alpha2(cn_name_format)

    if len(cn_name) == 3:
        return country_alpha3_to_country_alpha2(cn_name)

    if len(cn_name) == 2:
        if cn_name not in list_country_alpha2:
            raise KeyError(f"Invalid Country Alpha-2 code: '{cn_name}'")

        return cn_name

    if cn_name not in dict_country_name_to_country_alpha2:
        raise KeyError(f"Invalid Country Name: '{cn_name}'")

    return dict_country_name_to_country_alpha2[cn_name]


def country_name_to_country_alpha3(
    cn_name: str,
    cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT,
) -> str:
    """Convert a country name or code to an ISO 3166-1 alpha-3 code.

    Parameters
    ----------
    cn_name : str
        Country name or alpha-3 code to resolve.
    cn_name_format : str, default="default"
        Letter-case format used when matching country names.

    Returns
    -------
    str
        The corresponding three-letter country code.

    Raises
    ------
    KeyError
        If the country name or code is missing or is not recognized.
    """
    if cn_name is None:
        raise KeyError(f"Invalid Country Name: '{cn_name}'")

    cn_name = country_name_format(cn_name, cn_name_format)
    dict_country_name_to_country_alpha3 = map_country_name_to_country_alpha3(cn_name_format)

    if len(cn_name) == 3:
        from .country_mappings import list_country_alpha3

        list_country_alpha3 = list_country_alpha3()
        if cn_name not in list_country_alpha3:
            raise KeyError(f"Invalid Country Alpha-3 code: '{cn_name}'")

        return cn_name

    if cn_name not in dict_country_name_to_country_alpha3:
        raise KeyError(f"Invalid Country Name: '{cn_name}'")

    return dict_country_name_to_country_alpha3[cn_name]
