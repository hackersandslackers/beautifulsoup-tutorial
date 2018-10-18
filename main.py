import beautifulsoup4
import flask

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
            plaintext = request_json['plain']
            html = request_json['html']
            return html
        else:
            return 'nothing happened'
