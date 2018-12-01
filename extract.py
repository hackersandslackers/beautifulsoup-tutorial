import requests
from bs4 import BeautifulSoup


def get_links(html, headers):
    """Extract links from url."""
    r = requests.get(html, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.select('.post-content').find_all('a').get('href')
    return links
