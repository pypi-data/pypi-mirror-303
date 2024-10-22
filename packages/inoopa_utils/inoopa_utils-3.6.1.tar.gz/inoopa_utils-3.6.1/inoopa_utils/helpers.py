from tldextract import extract


def extract_domain(url: str) -> str:
    """
    Extract the domain from a url. We dedicate a function here to make sure we do it the same way everywhere.

    ex: https://www.inoopa.com/contact -> inoopa.com
    """
    # if http is not present, we can't parse the domain
    if "https://" in url and "http://" not in url:
        url = "http://" + url
    return extract(url).registered_domain
