"""Scrape metadata from target URL."""
import pprint

from beautifulsoup_tutorial.fetch import fetch_html_from_url
from beautifulsoup_tutorial.scrape import scrape_page_metadata

from config import TARGET_URL


def init_script() -> dict:
    """
    Fetch a given HTML page to extract & display metadata for.

    returns: dict
    """
    resp = fetch_html_from_url(TARGET_URL)
    metadata = scrape_page_metadata(resp, TARGET_URL)
    pp = pprint.PrettyPrinter(indent=4, width=120, sort_dicts=False)
    pp.pprint(metadata)
    return metadata
