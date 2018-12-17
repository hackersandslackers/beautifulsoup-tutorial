import requests
from bs4 import BeautifulSoup
from fallback import get_title, get_description, get_image, get_site_name


def get_meta(link, headers):
    """Generate preview obj per link."""
    exception_domains = ['Youtube', 'Medium' 'Github']
    r = requests.get(link, headers=headers)
    embedded_link = BeautifulSoup(r.content, 'html.parser')
    domain = get_site_name(embedded_link, link)
    if domain in exception_domains:
        print('WARNING:', domain)
    preview_dict = {
        'title': get_title(embedded_link),
        'description': get_description(embedded_link),
        'image': get_image(embedded_link),
        'sitename': get_site_name(embedded_link, link),
        'url': link
        }
    return preview_dict
