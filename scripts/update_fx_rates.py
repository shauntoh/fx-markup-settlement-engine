#!/usr/bin/env python3
"""Fetch ECB reference rates and generate fx_rates.json."""

from __future__ import annotations

import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "fx_rates.json"


def fetch_xml(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_rates(xml_text: str) -> tuple[str, dict[str, float]]:
    ns = {"gesmes": "http://www.gesmes.org/xml/2002-08-01", "e": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref"}
    root = ET.fromstring(xml_text)

    cube_time = root.find(".//e:Cube[@time]", ns)
    if cube_time is None:
        raise ValueError("Could not find dated Cube node in ECB feed")

    as_of = cube_time.attrib["time"]
    rates: dict[str, float] = {"EUR": 1.0}

    for cube in cube_time.findall("e:Cube", ns):
        currency = cube.attrib.get("currency")
        rate = cube.attrib.get("rate")
        if currency and rate:
            rates[currency] = float(rate)

    return as_of, rates


def build_payload(as_of: str, eur_rates: dict[str, float]) -> dict:
    return {
        "meta": {
            "source": "ECB Reference Rates",
            "as_of": as_of,
        },
        "rates": {
            "EUR": eur_rates,
        },
    }


def main() -> None:
    xml_text = fetch_xml(ECB_URL)
    as_of, eur_rates = parse_rates(xml_text)
    payload = build_payload(as_of, eur_rates)

    OUTPUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {len(eur_rates)} EUR-based rates for {as_of}.")


if __name__ == "__main__":
    main()
