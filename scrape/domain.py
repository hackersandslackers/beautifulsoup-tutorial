def get_domain(url):
    """Get site root domain name."""
    domain = url.split('//')[1]
    name = domain.split('/')[0]
    return name