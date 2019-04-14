import requests
from bs4 import BeautifulSoup
from fetch import get_title, get_description, get_image, get_site_name


def get_meta(link):
    """Generate preview obj per link.

    1. Determine title of target url.
    2. Create description blurb of target url.
    3. Find suitable image for target url.
    4. Determine the top-level site name of target url.
    5. Create dict of fetched metadata.
    6. Return result.
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    r = requests.get(link, headers=headers)
    embedded_link = BeautifulSoup(r.content, 'html.parser')
    preview_dict = {
        'title': get_title(embedded_link),
        'description': get_description(embedded_link),
        'image': get_image(embedded_link),
        'sitename': get_site_name(embedded_link, link),
        'url': link
        }
    return preview_dict
