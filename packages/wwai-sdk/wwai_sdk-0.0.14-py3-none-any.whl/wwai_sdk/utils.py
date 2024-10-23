import requests


def down_bytes(url):
    try:
        from PIL import Image
    except ImportError:
        raise ImportError("Please install PIL with `pip install Pillow`")

    resp = requests.get(url, verify=False)
    if resp.status_code != 200:
        raise Exception(resp.status_code, resp.content)
    return resp.content


def is_url(s):
    s = s.lower()
    if s.startswith('http://') or s.startswith('https://'):
        return True
    return False