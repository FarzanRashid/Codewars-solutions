def remove_url_anchor(url):
    if url.count("#") == 1:
        url = url[:url.index("#")]
    return url