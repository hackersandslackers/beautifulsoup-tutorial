import os
import uuid
from main import scrape
import pytest

endpoint = 'https://us-central1-hackersandslackers-204807.cloudfunctions.net/Hackers-lynx?url='
passed_url = 'https://hackersandslackers.com/p/2ee7075c-c495-4d91-adde-fd90b1442189/'

@pytest.fixture(scope="module", params=[endpoint+passed_url])

'''@pytest.fixture
def scrape_test():
    '''Returns a Wallet instance with a zero balance'''
    assert scrape(endpoint+passed_url)
'''
