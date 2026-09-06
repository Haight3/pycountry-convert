#  @namespace pycountry-convert

import pprintpp

import resources.data.get_countries_wikipedia as get_countries_wikipedia

pprintpp.pprint(get_countries_wikipedia.get_alpha3_codes_to_alpha2_codes_from_wiki())
