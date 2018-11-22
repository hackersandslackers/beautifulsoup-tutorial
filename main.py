import requests
from bs4 import BeautifulSoup
from flask import make_response
from extract import getLinks
from meta import getMeta


def scrape(request):
    """Scrape scheduled link previews."""
    if request.method == 'POST':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        target_url = request.args.get('url')
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
        links = getLinks(target_url, headers)
        previews = getMeta(links, headers)
        return make_response(previews, 200, headers)
    return make_response('bruh pls', 400, headers)
