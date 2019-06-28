def get_site_name(link, url):
    """Attempt to get the site's base name.

    1. Check OG tags for site name.
    2. If no OG tag exists, get top-level domain from url.
    3. Return site name.
    """
    sitename = None
    if link.find("meta", property="og:site_name"):
        sitename = link.find("meta", property="og:site_name").get('content')
    else:
        sitename = url.split('//')[1]
        name = sitename.split('/')[0]
        name = sitename.rsplit('.')[1]
        return name.capitalize()
    return sitename