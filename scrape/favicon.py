def get_favicon(link):
    """Fetch favicon."""
    favicon = None
    if link.find("link", attrs={"rel": "icon"}):
        favicon = link.find("link", attrs={"rel": "icon"}).get('href')
    elif link.find("link", attrs={"rel": "shortcut icon"}):
        favicon = link.find("link", attrs={"rel": "shortcut icon"}).get('href')
    return favicon