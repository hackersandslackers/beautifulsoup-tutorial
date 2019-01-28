from flask import make_response, request
from fetch import get_meta
import json


def scrape(request):
    """Scrape scheduled link previews."""
    # Allows POST requests from any origin with the Content-Type
    # header and caches preflight response for an 3600s
    target_url = request.args.get('url')
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    previews = get_meta(target_url, headers)
    response_body = json.dumps(previews)
    return make_response(str(response_body), 200, headers)
