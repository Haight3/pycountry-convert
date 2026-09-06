#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import resources.data.get_countries_wikipedia as get_countries_wikipedia
import pprintpp
pprintpp.pprint(get_countries_wikipedia.get_alpha3_codes_to_alpha2_codes_from_wiki())