import requests
from bs4 import BeautifulSoup
from flask import make_response
from urllib.request import urlretrieve
import time


def getTitle(linked_preview):
    """Attempt to get a title."""
    title = ''
    if linked_preview.title.string is not None:
        title = linked_preview.title.string
    elif linked_preview.find("h1") is not None:
        title = linked_preview.find("h1")[0]
    return title


def getDescription(linked_preview):
    """Attempt to get description."""
    description = 'EMPTY'
    if linked_preview.find("meta", property="og:description") is not None:
        description = linked_preview.find("meta", property="og:description").get('content')
    elif linked_preview.find("p") is not None:
        description = linked_preview.find("p").content
    return description


def getImage(linked_preview):
    """Attempt to get image."""
    image = ''
    if linked_preview.find("meta", property="og:image") is not None:
        image = linked_preview.find("meta", property="og:image").get('content')
        # store_image(image)
    elif linked_preview.find("img") is not None:
        image = linked_preview.find("img").get('href')
    return image


def getSiteName(linked_preview):
    """Attempt to get the site's base name."""
    sitename = ''
    if linked_preview.find("meta", property="og:site_name") is not None:
        sitename = linked_preview.find("meta", property="og:site_name").get('content')
    else:
        sitename = linked_preview.url
    return sitename


def scrape(request):
    """Scrape scheduled link previews."""
    if request.method == 'POST':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        request_json = request.get_json()
        ghost_url = request_json['url']
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
        r = requests.get(ghost_url)
        raw_html = r.content
        html = BeautifulSoup(raw_html, 'html.parser')
        body = html.select('.post-content p > a')
        previews = []
        print('previews =', previews)
        for link in body:
            url = link.get('href')
            r2 = requests.get(url, headers=headers)
            link_html = r2.content
            linked_preview = BeautifulSoup(link_html, 'html.parser')
            print('linked_preview', url)
            preview_dict = {
                'title': getTitle(linked_preview),
                'description': getDescription(linked_preview),
                'image': getImage(linked_preview),
                'sitename': getSiteName(linked_preview),
                'url': url
                }
            previews.append(preview_dict)
        return make_response(str(previews), 200, headers)
