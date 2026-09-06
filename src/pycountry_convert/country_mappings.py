"""
Country Mapping Builders
========================
*Created on 2026-09-06 by Isbert*
*Copyright (C) 2018 TUNE, Inc. (http://www.tune.com)*
*For COPYING and LICENSE details, please refer to the LICENSE file*

This module builds cached mappings among country names, ISO 3166-1 codes, and
official country names from pycountry data and supported Wikipedia aliases.
"""

from functools import lru_cache

from .country_name_format import COUNTRY_NAME_FORMAT_DEFAULT, country_name_format
from .country_wikipedia import WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2


@lru_cache(maxsize=128)
def map_countries(
    cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT,
    cn_extra: dict[str, str] = {},
) -> dict[str, dict[str, str]]:
    """Build a mapping of country names to ISO 3166-1 identifiers.

    Parameters
    ----------
    cn_name_format : str, default="default"
        Letter-case format to apply to country-name keys.
    cn_extra : dict[str, str], optional
        Additional country-name aliases mapped to alpha-2 country codes.

    Returns
    -------
    dict[str, dict[str, str]]
        Country names mapped to their alpha-2, alpha-3, and numeric codes.

    Raises
    ------
    KeyError
        If an additional alias refers to an invalid country code or cannot be
        resolved to a mapped country name.

    Notes
    -----
    Results are cached, so explicitly supplied arguments must be hashable.
    """
    from pycountry import countries

    from .convert_countries import country_alpha2_to_country_name

    dict_countries = {}

    for cn in countries:
        cn_name = country_name_format(cn.name, cn_name_format)
        dict_countries.update({cn_name: {"alpha_2": cn.alpha_2, "alpha_3": cn.alpha_3, "numeric": cn.numeric}})

        if hasattr(cn, "official_name"):
            cn_name = country_name_format(cn.official_name, cn_name_format)
            dict_countries.update({cn_name: {"alpha_2": cn.alpha_2, "alpha_3": cn.alpha_3, "numeric": cn.numeric}})

        if hasattr(cn, "common_name"):
            cn_name = country_name_format(cn.common_name, cn_name_format)
            dict_countries.update({cn_name: {"alpha_2": cn.alpha_2, "alpha_3": cn.alpha_3, "numeric": cn.numeric}})

    # Wikipedia Country Names
    for cn_name_wiki, cn_alpha2 in WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2.items():
        cn_name_wiki = country_name_format(cn_name_wiki, cn_name_format)

        if cn_name_wiki in dict_countries:
            # pprint(f"Skip: {cn_name_wiki}: {cn_alpha2}")
            continue

        try:
            cn_name = country_alpha2_to_country_name(cn_alpha2, cn_name_format)
        except KeyError:
            # pprint(f"Miss: {cn_name_wiki}: {cn_alpha2}")
            continue

        if cn_name not in dict_countries:
            raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

        # pprint(f"Add: {cn_name_wiki}: {cn_alpha2}")
        dict_countries.update({cn_name_wiki: dict_countries[cn_name]})

    # Extra Country Names
    for cn_name_extra, cn_alpha2 in cn_extra.items():
        cn_name_extra = country_name_format(cn_name_extra, cn_name_format)

        if cn_name_extra in dict_countries:
            continue

        try:
            cn_name = country_alpha2_to_country_name(cn_alpha2, cn_name_format)
        except KeyError:
            raise

        if cn_name not in dict_countries:
            raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

        dict_countries.update({cn_name_extra: dict_countries[cn_name]})

    return dict_countries


@lru_cache(maxsize=128)
def map_country_name_to_country_alpha2(cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map country names to ISO 3166-1 alpha-2 codes.

    Parameters
    ----------
    cn_name_format : str, default="default"
        Letter-case format to apply to country-name keys.

    Returns
    -------
    dict[str, str]
        Country names mapped to two-letter country codes.
    """
    return {key: value["alpha_2"] for key, value in map_countries(cn_name_format).items()}


@lru_cache(maxsize=128)
def map_country_name_to_country_alpha3(cn_name_format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map country names to ISO 3166-1 alpha-3 codes.

    Parameters
    ----------
    cn_name_format : str, default="default"
        Letter-case format to apply to country-name keys.

    Returns
    -------
    dict[str, str]
        Country names mapped to three-letter country codes.
    """
    return {key: value["alpha_3"] for key, value in map_countries(cn_name_format).items()}


@lru_cache(maxsize=128)
def map_country_alpha2_to_country_name(format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map ISO 3166-1 alpha-2 codes to country names.

    Parameters
    ----------
    format : str, default="default"
        Letter-case format to apply to country names.

    Returns
    -------
    dict[str, str]
        Two-letter country codes mapped to country names.
    """
    import pycountry

    return {x.alpha_2: country_name_format(x.name, format) for x in pycountry.countries}


@lru_cache(maxsize=128)
def get_country_alpha2_to_country_official_name(format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map ISO 3166-1 alpha-2 codes to official country names.

    Parameters
    ----------
    format : str, default="default"
        Letter-case format to apply to official country names.

    Returns
    -------
    dict[str, str]
        Two-letter country codes mapped to official country names.
    """
    import pycountry

    return {x.alpha_2: country_name_format(x.official_name, format) for x in pycountry.countries}


@lru_cache(maxsize=128)
def map_country_alpha3_to_country_name(format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map ISO 3166-1 alpha-3 codes to country names.

    Parameters
    ----------
    format : str, default="default"
        Letter-case format to apply to country names.

    Returns
    -------
    dict[str, str]
        Three-letter country codes mapped to country names.
    """
    import pycountry

    return {x.alpha_3: country_name_format(x.name, format) for x in pycountry.countries}


@lru_cache(maxsize=128)
def get_country_alpha3_to_country_official_name(format: str = COUNTRY_NAME_FORMAT_DEFAULT) -> dict[str, str]:
    """Map ISO 3166-1 alpha-3 codes to official country names.

    Parameters
    ----------
    format : str, default="default"
        Letter-case format to apply to official country names.

    Returns
    -------
    dict[str, str]
        Three-letter country codes mapped to official country names.
    """
    import pycountry

    return {x.alpha_3: country_name_format(x.official_name, format) for x in pycountry.countries}


@lru_cache(maxsize=128)
def map_country_alpha3_to_country_alpha2() -> dict[str, str]:
    """Map ISO 3166-1 alpha-3 codes to alpha-2 codes.

    Returns
    -------
    dict[str, str]
        Three-letter country codes mapped to two-letter country codes.
    """
    import pycountry

    return {x.alpha_3: x.alpha_2 for x in pycountry.countries}


@lru_cache(maxsize=128)
def map_country_alpha2_to_country_alpha3() -> dict[str, str]:
    """Map ISO 3166-1 alpha-2 codes to alpha-3 codes.

    Returns
    -------
    dict[str, str]
        Two-letter country codes mapped to three-letter country codes.
    """
    import pycountry

    return {x.alpha_2: x.alpha_3 for x in pycountry.countries}


@lru_cache(maxsize=128)
def list_country_alpha2() -> list[str]:
    """Return all ISO 3166-1 alpha-2 country codes.

    Returns
    -------
    list[str]
        Two-letter country codes provided by pycountry.
    """
    import pycountry

    return [x.alpha_2 for x in pycountry.countries]


@lru_cache(maxsize=128)
def list_country_alpha3() -> list[str]:
    """Return all ISO 3166-1 alpha-3 country codes.

    Returns
    -------
    list[str]
        Three-letter country codes provided by pycountry.
    """
    import pycountry

    return [x.alpha_3 for x in pycountry.countries]
