"""Behavioral tests for the public country conversion API."""

from collections.abc import Callable

import pytest

import pycountry_convert as pc


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
    """Convert representative alpha-2 codes from every continent."""
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
    """Convert every supported continent code to its display name."""
    assert pc.convert_continent_code_to_continent_name(code) == expected_name


def test_alpha3_to_continent_name_chain() -> None:
    """Resolve a continent name from an alpha-3 code through the public API."""
    alpha2 = pc.country_alpha3_to_country_alpha2("DEU")
    continent_code = pc.country_alpha2_to_continent_code(alpha2)

    assert pc.convert_continent_code_to_continent_name(continent_code) == "Europe"


def test_country_conversions() -> None:
    """Exercise each public country conversion path."""
    assert pc.country_alpha2_to_country_name("DE") == "Germany"
    assert pc.country_alpha3_to_country_alpha2("DEU") == "DE"
    assert pc.country_name_to_country_alpha2("Germany") == "DE"
    assert pc.country_name_to_country_alpha3("Germany") == "DEU"


def test_country_name_converter_accepts_country_codes() -> None:
    """Resolve alpha-2 and alpha-3 inputs through the country-name entrypoint."""
    assert pc.country_name_to_country_alpha2("DE") == "DE"
    assert pc.country_name_to_country_alpha2("DEU") == "DE"


@pytest.mark.parametrize(
    ("name", "expected_alpha2"),
    [
        ("Great Britain", "GB"),
        ("South Korea", "KR"),
        ("Ivory Coast", "CI"),
        ("Republic of the Congo", "CG"),
    ],
)
def test_wikipedia_country_aliases(name: str, expected_alpha2: str) -> None:
    """Resolve supported Wikipedia aliases to alpha-2 codes."""
    assert pc.country_name_to_country_alpha2(name) == expected_alpha2


def test_country_name_formats() -> None:
    """Apply the supported lower- and upper-case country-name formats."""
    assert pc.country_alpha2_to_country_name("DE", pc.COUNTRY_NAME_FORMAT_UPPER) == "GERMANY"
    assert pc.country_alpha2_to_country_name("DE", pc.COUNTRY_NAME_FORMAT_LOWER) == "germany"
    assert pc.country_name_to_country_alpha2("GERMANY", pc.COUNTRY_NAME_FORMAT_UPPER) == "DE"
    assert pc.country_name_to_country_alpha2("germany", pc.COUNTRY_NAME_FORMAT_LOWER) == "DE"


def test_mapping_api() -> None:
    """Build the public mappings and country-code lists from real pycountry data."""
    assert pc.map_country_alpha3_to_country_alpha2()["DEU"] == "DE"
    assert pc.map_country_alpha2_to_country_alpha3()["DE"] == "DEU"
    assert pc.map_country_alpha2_to_country_name()["DE"] == "Germany"
    assert pc.map_country_name_to_country_alpha2()["Germany"] == "DE"


@pytest.mark.parametrize(
    "conversion",
    [
        pc.country_alpha2_to_country_name,
        pc.country_alpha2_to_continent_code,
    ],
)
@pytest.mark.parametrize("invalid_alpha2", [None, "", "D", "ZZ"])
def test_invalid_alpha2_raises_key_error(
    conversion: Callable[[str | None], str],
    invalid_alpha2: str | None,
) -> None:
    """Reject invalid alpha-2 values across public alpha-2 entrypoints."""
    with pytest.raises(KeyError):
        conversion(invalid_alpha2)


@pytest.mark.parametrize("invalid_code", [None, "", "E", "XX"])
def test_invalid_continent_code_raises_key_error(invalid_code: str | None) -> None:
    """Reject missing, malformed, and unknown continent codes."""
    with pytest.raises(KeyError):
        pc.convert_continent_code_to_continent_name(invalid_code)


@pytest.mark.parametrize(
    ("conversion", "invalid_value"),
    [
        (pc.country_alpha3_to_country_alpha2, None),
        (pc.country_alpha3_to_country_alpha2, "ZZZ"),
        (pc.country_name_to_country_alpha2, None),
        (pc.country_name_to_country_alpha2, "Atlantis"),
        (pc.country_name_to_country_alpha3, None),
        (pc.country_name_to_country_alpha3, "Atlantis"),
    ],
)
def test_invalid_country_identifier_raises_key_error(
    conversion: Callable[[str | None], str],
    invalid_value: str | None,
) -> None:
    """Reject unknown alpha-3 codes and country names."""
    with pytest.raises(KeyError):
        conversion(invalid_value)
