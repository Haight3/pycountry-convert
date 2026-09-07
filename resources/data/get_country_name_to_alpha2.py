#  @namespace pycountry-convert

import pprintpp

from resources.data import get_countries_wikipedia

pprintpp.pprint(get_countries_wikipedia.get_alpha3_codes_to_alpha2_codes_from_wiki())
