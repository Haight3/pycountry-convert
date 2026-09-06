"""Regression tests for the legacy conversion API."""

import pytest

import pycountry_convert as pc


def test_alpha2_to_continent() -> None:
    """Convert an alpha-2 code to its continent."""
    assert pc.convert_country_alpha2_to_continent("DE") == "Europe"
    assert pc.convert_country_alpha2_to_continent("JP") == "Asia"


def test_alpha3_to_alpha2() -> None:
    """Convert an alpha-3 code to alpha-2."""
    assert pc.convert_country_alpha3_to_country_alpha2("DEU") == "DE"
    assert pc.convert_country_alpha3_to_country_alpha2("JPN") == "JP"


def test_alpha3_to_continent_chain() -> None:
    """Resolve a continent from an alpha-3 code through the public API."""
    alpha2 = pc.convert_country_alpha3_to_country_alpha2("DEU")
    assert pc.convert_country_alpha2_to_continent(alpha2) == "Europe"


def test_country_name_conversions() -> None:
    """Convert between country names and alpha-2 codes."""
    assert pc.convert_country_name_to_country_alpha2("Germany") == "DE"
    assert pc.convert_country_alpha2_to_country_name("DE") == "Germany"


def test_unknown_alpha2_raises_key_error() -> None:
    """Preserve the legacy error behavior for an unknown alpha-2 code."""
    with pytest.raises(KeyError):
        pc.convert_country_alpha2_to_continent("ZZ")


def test_unknown_alpha3_raises_key_error() -> None:
    """Preserve the legacy error behavior for an unknown alpha-3 code."""
    with pytest.raises(KeyError):
        pc.convert_country_alpha3_to_country_alpha2("ZZZ")
