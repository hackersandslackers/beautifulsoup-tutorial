from flask import Flask, make_response, request, jsonify
from scrape import fetch


def scrape(request):
    """Scrape URL provided in querystring param to create preview."""
    target_url = request.args.get('url')
    if target_url:
        previews = fetch.get_meta(target_url)
        response = jsonify(previews)
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST'
        }
        return make_response(response, 200, headers)
    return make_response("You must provide a `url` parameter.", 500, headers)
