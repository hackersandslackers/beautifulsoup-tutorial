import requests
from bs4 import BeautifulSoup
from fetch import get_title, get_description, get_image, get_site_name


def get_meta(link, headers):
    """Generate preview obj per link.

    1. Determine title of target url.
    2. Create description blurb of target url.
    3. Find suitable image for target url.
    4. Determine the top-level site name of target url.
    5. Create dict of fetched metadata.
    6. Return result.
    """
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
