"""Scrape metadata attributes from a requested URL."""
from typing import Optional

from bs4 import BeautifulSoup
from requests import Response


def scrape_page_metadata(resp: Response, url: str) -> dict:
    """
    Parse page & return metadata.

    :param Response resp: Raw HTTP response.
    :param str url: URL of targeted page.

    :return: dict
    """
    html = BeautifulSoup(resp.content, "html.parser")
    metadata = {
        "title": get_title(html),
        "description": get_description(html),
        "image": get_image(html),
        "favicon": get_favicon(html, url),
        "theme_color": get_theme_color(html),
    }
    return metadata


def get_title(html: BeautifulSoup) -> Optional[str]:
    """
    Scrape page title with multiple fallbacks.

    :param BeautifulSoup html: Parsed HTML object.
    :param str url: URL of targeted page.

    :returns: Optional[str]
    """
    title = html.title.string
    if title:
        return title
    elif html.find("meta", property="og:title"):
        return html.find("meta", property="og:title").get("content")
    return html.find("h1").string


def get_description(html: BeautifulSoup) -> Optional[str]:
    """
    Scrape page description.

    :param BeautifulSoup html: Parsed HTML object.
    :param str url: URL of targeted page.

    :returns: Optional[str]
    """
    description = html.find("meta", property="description")
    if description:
        return description.get("content")
    elif html.find("meta", property="og:description"):
        return html.find("meta", property="og:description").get("content")
    return html.p.string


def get_image(html: BeautifulSoup) -> Optional[str]:
    """
    Scrape preview image.

    :param BeautifulSoup html: Parsed HTML object.

    :returns: Optional[str]
    """
    image = html.find("meta", property="image")
    if image:
        return image.get("content")
    elif html.find("meta", {"property": "og:image"}):
        return html.find("meta", {"property": "og:image"}).get("content")
    return html.img.src


def get_favicon(html: BeautifulSoup, url: str) -> Optional[str]:
    """
    Scrape favicon from `icon`, or fallback to conventional favicon.

    :param Response resp: Raw HTTP response.
    :param str url: URL of targeted page.

    :returns: Optional[str]
    """
    if html.find("link", attrs={"rel": "icon"}):
        return html.find("link", attrs={"rel": "icon"}).get("href")
    elif html.find("link", attrs={"rel": "shortcut icon"}):
        return html.find("link", attrs={"rel": "shortcut icon"}).get("href")
    return f"{url.rstrip('/')}/favicon.ico"


def get_theme_color(html: BeautifulSoup) -> Optional[str]:
    """
    Scrape brand color.

    :param BeautifulSoup html: Parsed HTML object.

    :returns: Optional[str]
    """
    if html.find("meta", {"name": "theme-color"}):
        return html.find("meta", {"name": "theme-color"}).get("content")
