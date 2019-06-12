from flask import Flask, make_response, request, jsonify
from fetch import get_meta


def scrape(request):
    """Scrape URL provided in querystring param to create preview."""
    target_url = request.args.get('url')
    previews = get_meta(target_url)
    response = jsonify(previews)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response
