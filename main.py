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

        request_json = request.get_json()
        if request_json:

            url = request_json['url']
            plaintext = request_json['plain']
            html = request_json['html']
            soup = BeautifulSoup(url, 'html.parser')
            arr = []
            for link in soup['post-content'].find_all('a'):
                arr.append(link.get('href'))
            return arr
        else:
            return 'nothing happened'
