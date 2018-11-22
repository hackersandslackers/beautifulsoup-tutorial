import requests
from bs4 import BeautifulSoup
from flask import make_response
from google.cloud import storage
from urllib.request import urlretrieve
import time


def store_image(source_file_name):
    """Upload preview image file to the bucket."""
    if source_file_name is not None:
        bucket_name = 'hackersandslackersassets'
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        destination_blob_name = source_file_name.rsplit('/')[-1]
        local_file = 'img/' + destination_blob_name
        urlretrieve(source_file_name, local_file)
        # delay to avoid corrupted previews
        time.sleep(1)
        blob = bucket.blob('linkpreviews/' + destination_blob_name)

        blob.upload_from_filename(local_file)

        print('File {} uploaded to {}.'.format(
            local_file,
            'linkpreviews/' + destination_blob_name))


def getTitle(link):
    """Attempt to get a title."""
    title = ''
    if link.title.string is not None:
        title = link.title.string
    elif link.find("h1") is not None:
        title = link.find("h1")
    return title


def getDescription(link):
    """Attempt to get description."""
    description = 'EMPTY'
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.find("p").content
    return description


def getImage(link):
    """Attempt to get a preview image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image


def getSiteName(link, url):
    """Attempt to get the site's base name."""
    sitename = ''
    if link.find("meta", property="og:site_name") is not None:
        sitename = link.find("meta", property="og:site_name").get('content')
    else:
        sitename = url.split('//')[1]
        name = sitename.split('/')[0]
        name = sitename.rsplit('.')[1]
        return name.capitalize()
    return sitename


def scrape(targeturl):
    """Scrape scheduled link previews."""
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    r = requests.get(targeturl)
    raw_html = r.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    links = soup.select('.post-content p > a')
    previews = []
    print('previews =', previews)
    for link in links:
        url = link.get('href')
        r2 = requests.get(url, headers=headers)
        link_html = r2.content
        embedded_link = BeautifulSoup(link_html, 'html.parser')
        print('embedded_link', url)
        preview_dict = {
            'title': getTitle(embedded_link),
            'description': getDescription(embedded_link),
            'image': getImage(embedded_link),
            'sitename': getSiteName(embedded_link, url),
            'url': url
            }
        previews.append(preview_dict)
        print(preview_dict)
    return make_response(str(previews), 200, headers)


scrape()
