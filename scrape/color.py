def get_theme_color(link):
    """Get brand color."""
    if link.find("meta", property="theme-color"):
        color = link.find("meta", property="theme-color").get('content')
        return color
    return None