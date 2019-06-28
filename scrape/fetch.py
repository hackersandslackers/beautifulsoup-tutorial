import requests
from bs4 import BeautifulSoup
from .color import get_theme_color
from .favicon import get_favicon
from .title import get_title
from .image import get_image
from .domain import get_domain
from .name import get_site_name
from .description import get_description


def get_meta(link):
    """Generate object summarizing target link data."""
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
        'favicon': get_favicon(embedded_link),
        'sitename': get_site_name(embedded_link, link),
        'color': get_theme_color(embedded_link, link),
        'url': link
        }
    return preview_dict
