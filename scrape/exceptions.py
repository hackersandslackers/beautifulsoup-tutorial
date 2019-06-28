'''def site_exceptions(link, url):
    """Check to see if site is in list of exceptions."""
    domain = get_site_name(link, url)
    exception_domains = ['Youtube', 'Medium' 'Github']
    if domain in exception_domains:
        print('WARNING:', domain)'''