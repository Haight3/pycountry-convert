"""
Country Conversion Package
==========================
*Created on 2026-09-06 by ibaris*
*Copyright (C) 2026 Haight Labs (https://www.haight.ai)*
*Copyright (C) 2018 TUNE, Inc. (http://www.tune.com)*
*For COPYING and LICENSE details, please refer to the LICENSE file*

This package exposes country, ISO code, and continent conversion helpers along
with the mapping and country-name formatting utilities used by those helpers.
"""

__version__ = "2026.9.1"


from .convert_continent_code_to_continent_name import convert_continent_code_to_continent_name
from .convert_countries import (
    country_alpha2_to_country_name,
    country_alpha3_to_country_alpha2,
    country_name_to_country_alpha2,
    country_name_to_country_alpha3,
)
from .convert_country_alpha2_to_continent_code import country_alpha2_to_continent_code
from .country_mappings import (
    map_countries,
    map_country_alpha2_to_country_alpha3,
    map_country_alpha2_to_country_name,
    map_country_alpha3_to_country_alpha2,
    map_country_alpha3_to_country_name,
    map_country_name_to_country_alpha2,
    map_country_name_to_country_alpha3,
)
from .country_name_format import COUNTRY_NAME_FORMAT_DEFAULT, COUNTRY_NAME_FORMAT_LOWER, COUNTRY_NAME_FORMAT_UPPER, country_name_format
from .country_wikipedia import WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2
