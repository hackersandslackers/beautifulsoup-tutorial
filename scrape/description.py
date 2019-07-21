def get_description(link):
    """Attempt to get description.

    1. Check OG tags for description tag.
    2. If doesn't exist, check page for p tag.
    3, Return description.
    """
    description = None
    if link.find("meta", property="description"):
        description = link.find("meta", property="description").get('content')
    elif link.find("meta", property="og:description"):
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p"):
        description = link.find("p").contents
    return description