import requests
from bs4 import BeautifulSoup


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
        for a in html.select('a'):
			url = link.get('href')
            links.append(url)
            #r = requests.get(url)
            #print(r.text)
        return links
        #else:
            #return "no body sent wtf"
