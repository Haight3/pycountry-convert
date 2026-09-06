"""Behavioral tests for the public country conversion API."""

from collections.abc import Callable

import pytest

import pycountry_convert as pc


@pytest.mark.parametrize(
    ("alpha2", "expected_continent"),
    [
        ("DE", "Europe"),
        ("JP", "Asia"),
        ("ZA", "Africa"),
        ("US", "North America"),
        ("BR", "South America"),
        ("AU", "Oceania"),
        ("BV", "Antarctica"),
    ],
)
def test_alpha2_to_continent(alpha2: str, expected_continent: str) -> None:
    """Convert representative alpha-2 codes from every continent."""
    assert pc.convert_country_alpha2_to_continent(alpha2) == expected_continent


@pytest.mark.parametrize(
    ("alpha3", "expected_alpha2"),
    [
        ("DEU", "DE"),
        ("JPN", "JP"),
        ("USA", "US"),
        ("ZAF", "ZA"),
    ],
)
def test_alpha3_to_alpha2(alpha3: str, expected_alpha2: str) -> None:
    """Convert representative alpha-3 codes to alpha-2."""
    assert pc.convert_country_alpha3_to_country_alpha2(alpha3) == expected_alpha2


def test_alpha3_to_continent_chain() -> None:
    """Resolve a continent from an alpha-3 code through the public API."""
    alpha2 = pc.convert_country_alpha3_to_country_alpha2("DEU")
    assert pc.convert_country_alpha2_to_continent(alpha2) == "Europe"


@pytest.mark.parametrize(
    ("alpha2", "expected_country_name"),
    [
        ("DE", "Germany"),
        ("US", "United States of America"),
        ("CI", "Ivory Coast"),
        ("XK", "Kosovo"),
    ],
)
def test_alpha2_to_country_name(alpha2: str, expected_country_name: str) -> None:
    """Convert representative alpha-2 codes to country names."""
    assert pc.convert_country_alpha2_to_country_name(alpha2) == expected_country_name


@pytest.mark.parametrize(
    ("country_name", "expected_alpha2"),
    [
        ("Germany", "DE"),
        ("United States", "US"),
        ("Great Britain", "GB"),
        ("Republic of the Congo", "CG"),
    ],
)
def test_country_name_to_alpha2(country_name: str, expected_alpha2: str) -> None:
    """Convert canonical country names and supported aliases to alpha-2."""
    assert pc.convert_country_name_to_country_alpha2(country_name) == expected_alpha2


def test_country_name_converter_accepts_alpha3_fallback() -> None:
    """Resolve an alpha-3 code through the country-name entrypoint."""
    assert pc.convert_country_name_to_country_alpha2("DEU") == "DE"


@pytest.mark.parametrize(
    "conversion",
    [
        pc.convert_country_alpha2_to_continent,
        pc.convert_country_alpha2_to_country_name,
    ],
)
def test_unknown_alpha2_raises_key_error(conversion: Callable[[str], str]) -> None:
    """Reject an unknown alpha-2 code across alpha-2 entrypoints."""
    with pytest.raises(KeyError):
        conversion("ZZ")


@pytest.mark.parametrize(
    ("conversion", "unknown_value"),
    [
        (pc.convert_country_alpha3_to_country_alpha2, "ZZZ"),
        (pc.convert_country_name_to_country_alpha2, "Atlantis"),
    ],
)
def test_unknown_country_identifier_raises_key_error(conversion: Callable[[str], str], unknown_value: str) -> None:
    """Reject unknown alpha-3 codes and country names."""
    with pytest.raises(KeyError):
        conversion(unknown_value)
