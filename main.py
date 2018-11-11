import requests
from bs4 import BeautifulSoup
from flask import make_response


def scrape(request):
    """Main request."""
    if request.method == 'POST':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        links = []
        request_json = request.get_json()
        ghost_url = request_json['url']
        r = requests.get(ghost_url)

        raw_html = r.text
        html = BeautifulSoup(raw_html, 'html.parser')
        body = html.select('.post-content')[0]
        links = body.select("p > a")
        previews = []
        print('previews =', previews)
        for link in links:
            url = link.get('href')
            r2 = requests.get(url)
            link_html = r2.text
            link_preview = BeautifulSoup(link_html, 'html.parser')
            d = link_preview.find("meta",  property="og:description")
            i = link_preview.find("meta",  property="og:image")
            try:
                title = link_preview.title.string
            except TypeError:
                title = 'site has no title'
            try:
                d.get('content')
            except TypeError:
                d = 'shitty site with no description'
            try:
                i.get('content')
            except TypeError:
                i = 'shitty site with no image'
            preview_dict = {
                'title': title,
                'description': d,
                'image': i,
                'url': url
            }
            previews.append(preview_dict)
        return make_response(str(previews), 200, headers)
