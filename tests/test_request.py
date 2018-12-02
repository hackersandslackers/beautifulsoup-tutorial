import flask
from bs4 import BeautifulSoup
import pytest
import requests

endpoint = 'https://us-central1-hackersandslackers-204807.cloudfunctions.net/Hackers-lynx?url='
passed_url = 'https://hackersandslackers.com/p/2ee7075c-c495-4d91-adde-fd90b1442189/'


@pytest.fixture(scope="module", params=[endpoint+passed_url])


@pytest.fixture
def receive_request(request):
    """Inspect incoming request."""
    target_url = request.args.get('url')
    assert target_url


@pytest.fixture
def inspect_html():
    """Inspect html of incoming page."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r, 'html.parser')
    assert soup
    assert soup.prettify()
