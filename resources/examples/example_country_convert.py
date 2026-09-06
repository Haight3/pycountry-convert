"""Small examples for the pycountry-convert-ng public API."""

import pycountry_convert as pc


def main() -> None:
    """Run representative country and continent conversions."""
    alpha2 = pc.country_alpha3_to_country_alpha2("DEU")
    continent_code = pc.country_alpha2_to_continent_code(alpha2)
    continent_name = pc.convert_continent_code_to_continent_name(continent_code)

    print("DEU ->", alpha2)
    print(alpha2, "->", continent_code, "->", continent_name)
    print("DE ->", pc.country_alpha2_to_country_name("DE"))
    print("Germany ->", pc.country_name_to_country_alpha2("Germany"))
    print("Germany ->", pc.country_name_to_country_alpha3("Germany"))
    print("Great Britain ->", pc.country_name_to_country_alpha2("Great Britain"))


if __name__ == "__main__":
    main()
