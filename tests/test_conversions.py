"""Behavioral tests for the pycountry-convert 0.7.2 public API."""

import pytest

import pycountry_convert as pc


def test_package_version() -> None:
    """Expose the maintained NG release version."""
    assert pc.__version__ == "2026.9.0"


@pytest.mark.parametrize(
    ("alpha2", "expected_code"),
    [
        ("DE", "EU"),
        ("JP", "AS"),
        ("ZA", "AF"),
        ("US", "NA"),
        ("BR", "SA"),
        ("AU", "OC"),
        ("BV", "AN"),
    ],
)
def test_alpha2_to_continent_code(alpha2: str, expected_code: str) -> None:
    """Convert representative alpha-2 codes to continent codes."""
    assert pc.country_alpha2_to_continent_code(alpha2) == expected_code


@pytest.mark.parametrize(
    ("code", "expected_name"),
    [
        ("EU", "Europe"),
        ("AS", "Asia"),
        ("AF", "Africa"),
        ("NA", "North America"),
        ("SA", "South America"),
        ("OC", "Oceania"),
        ("AN", "Antarctica"),
    ],
)
def test_continent_code_to_name(code: str, expected_name: str) -> None:
    """Convert continent codes to continent names."""
    assert pc.convert_continent_code_to_continent_name(code) == expected_name


def test_alpha3_to_continent_name_chain() -> None:
    """Resolve a continent name from an alpha-3 country code."""
    alpha2 = pc.country_alpha3_to_country_alpha2("DEU")
    continent_code = pc.country_alpha2_to_continent_code(alpha2)
    assert pc.convert_continent_code_to_continent_name(continent_code) == "Europe"


def test_country_conversions() -> None:
    """Exercise the main country conversion functions from 0.7.2."""
    assert pc.country_alpha2_to_country_name("DE") == "Germany"
    assert pc.country_alpha3_to_country_alpha2("DEU") == "DE"
    assert pc.country_name_to_country_alpha2("Germany") == "DE"
    assert pc.country_name_to_country_alpha3("Germany") == "DEU"


@pytest.mark.parametrize(
    ("name", "alpha2"),
    [
        ("Great Britain", "GB"),
        ("South Korea", "KR"),
        ("Ivory Coast", "CI"),
    ],
)
def test_wikipedia_country_aliases(name: str, alpha2: str) -> None:
    """Retain the additional Wikipedia country-name aliases."""
    assert pc.country_name_to_country_alpha2(name) == alpha2


def test_country_name_formats() -> None:
    """Support the original default/lower/upper name formatting modes."""
    assert pc.country_alpha2_to_country_name("DE", pc.COUNTRY_NAME_FORMAT_UPPER) == "GERMANY"
    assert pc.country_alpha2_to_country_name("DE", pc.COUNTRY_NAME_FORMAT_LOWER) == "germany"


def test_mapping_api() -> None:
    """Expose the mapping helpers added by the 0.7.x implementation."""
    assert pc.map_country_alpha3_to_country_alpha2()["DEU"] == "DE"
    assert pc.map_country_alpha2_to_country_alpha3()["DE"] == "DEU"
    assert pc.map_country_name_to_country_alpha2()["Germany"] == "DE"


@pytest.mark.parametrize("value", [None, "", "D", "ZZ"])
def test_invalid_alpha2_raises_key_error(value: str | None) -> None:
    """Reject invalid alpha-2 country codes."""
    with pytest.raises(KeyError):
        pc.country_alpha2_to_continent_code(value)


def test_invalid_continent_code_raises_key_error() -> None:
    """Reject invalid continent codes."""
    with pytest.raises(KeyError):
        pc.convert_continent_code_to_continent_name("XX")
