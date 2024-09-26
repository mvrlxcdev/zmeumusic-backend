from ytmusicapi import YTMusic

yt = YTMusic('oauth.json')


def search_with_filter(q: str, search_filter: str):
    return yt.search(query=q, filter=search_filter)
