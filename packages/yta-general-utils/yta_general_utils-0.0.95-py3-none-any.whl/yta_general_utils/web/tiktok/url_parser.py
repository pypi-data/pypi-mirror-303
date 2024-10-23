import requests


def __is_short_tiktok_url(url: str):
    # url like: https://vm.tiktok.com/ZGeSJ6YRA
    if not url:
        return False
    
    # TODO: Do this with a regexp
    if not '/' in url:
        return False
    
    url = __clean(url)
    
    if 'vm.tiktok.com' in url:
        return True
    
    return False

def __is_long_tiktok_url(url: str):
    # url like: https://www.tiktok.com/@ahorayasabesque/video/7327001175616703777?_t=8jqq93LWqsC&_r=1
    if not url:
        return False
    
    # TODO: Do this with a regexp
    if not '/' in url:
        return False
    
    url = __clean(url)

    if 'www.tiktok.com' in url:
        return True
    
    return False

def __short_tiktok_url_to_long_tiktok_url(url: str):
    """
    Transforms the provided short tiktok 'url' to 
    the long format and returns it.
    """
    if not url:
        raise Exception('No "url" provided.')
    
    if not __is_short_tiktok_url(url):
        raise Exception('No "url" provided is not a short tiktok url.')

    return requests.get(url).url

def __clean(url: str):
    """
    Removes any additional parameter that is after a
    question mark sign.
    """
    if not url:
        raise Exception('No "url" provided.')

    if '?' in url:
        url = url.split('?')[0]

    return url

def is_valid_tiktok_url(url: str):
    """
    This method returns True if the provided 'url' is a
    valid long or short tiktok video url or False if not.
    """
    return __is_short_tiktok_url(url) or __is_long_tiktok_url(url)

def parse_tiktok_url(url: str):
    """
    Parses the provided 'url' returning a dict with that
    'url' (long version) and also the 'username' and the
    'video_id' if it is a valid url. It will raise an 
    Exception if not valid 'url' provided.
    """
    if not url:
        raise Exception('No "url" provided.')

    if not is_valid_tiktok_url(url):
        raise Exception('The provided "url" is not a valid tiktok video url.')
    
    url = __clean(url)
    if not __is_long_tiktok_url(url):
        url = __short_tiktok_url_to_long_tiktok_url(url)

    aux = url.split('/')

    data = {
        'username': aux[len(aux) - 3],
        'video_id': aux[len(aux) - 1],
        'url': url,
    }

    return data
    

    