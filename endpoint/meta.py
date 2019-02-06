import requests
from bs4 import BeautifulSoup
from fallback import get_title, get_description, get_image, get_site_name


def get_meta(links, headers):
    """Generate preview obj per link."""
    previews = []
    exception_domains = ['Youtube', 'Medium' 'Github']
    for link in links:
        url = link.get('href')
        req = requests.get(url, headers=headers)
        embedded_link = BeautifulSoup(req.content, 'html.parser')
        domain = get_site_name(embedded_link, url)
        if domain in exception_domains:
            print('WARNING:', domain)
        preview_dict = {}
        if get_title(embedded_link):
            preview_dict['title'] = get_title(embedded_link)
        if get_description(embedded_link):
            preview_dict['description'] = get_description(embedded_link)
        if get_image(embedded_link):
            preview_dict['image'] = get_image(embedded_link)
        if get_site_name(embedded_link):
            preview_dict['sitename'] = get_site_name(embedded_link)
        preview_dict['url'] = url

        previews.append(preview_dict)
    return previews
