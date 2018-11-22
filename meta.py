import requests
from bs4 import BeautifulSoup
from fallback import get_title, get_description, get_image, get_site_name


def getMeta(links, headers):
    """Generate preview obj per link."""
    previews = []
    for link in links:
        url = link.get('href')
        r = requests.get(url, headers=headers)
        embedded_link = BeautifulSoup(r.content, 'html.parser')
        preview_dict = {
            'title': get_title(embedded_link),
            'description': get_description(embedded_link),
            'image': get_image(embedded_link),
            'sitename': get_site_name(embedded_link, url),
            'url': url
            }
        previews.append(preview_dict)
    return previews
