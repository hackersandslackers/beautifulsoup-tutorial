import re
from srl import SRL


def get_title(link):
    """Attempt to get a title."""
    title = ''
    if link.title.string is not None:
        title = link.title.string
    elif link.find("h1") is not None:
        title = link.find("h1")
    elif link.findall("h1") is not None:
        title = link.findall("h1")[0]
    return title


def get_description(link):
    """Attempt to get description."""
    description = 'EMPTY'
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.find("p").content
    elif link.findall("p") is not None:
        description = link.findall("p")[0]
    return description


def get_image(link):
    """Attempt to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.findall("img") is not None:
        image = link.findall("img")[0].get('href')
    return image


def get_site_name(link, url):
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
