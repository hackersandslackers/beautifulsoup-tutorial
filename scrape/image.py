def get_image(link):
    """Attempt to get image.

    1. Check OG tags for image tag.
    2. If doesn't exist, check page for img tag.
    3. If the image path is relative, make it absolute.
    4. Return image URL.
    """
    image = None
    if link.find("meta", property="image"):
        image = link.find("meta", property="image").get('content')
    elif link.find("meta", property="og:image"):
        image = link.find("meta", property="og:image").get('content')
    elif link.find_all("img", src=True):
        image = link.find_all("img")
        if image:
            image = link.find_all("img")[0].get('src')
    return image