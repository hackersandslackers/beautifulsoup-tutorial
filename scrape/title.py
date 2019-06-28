def get_title(link):
    """Attempt to get a title.

    1. Check metadata for title tag.
    2. If doesn't exist, check page for h1 tag.
    3. Remove all text which comes after the first pipe ("|") in the title.
    4. Return title.
    """
    title = None
    if link.title.string:
        title = link.title.string
    elif link.find("h1"):
        title = link.find("h1").string
    elif link.find_all("h1"):
        title = link.find_all("h1")[0].string
    if title:
        title = title.split('|')[0]
    return title