#!/usr/bin/env python3
"""
    In this tasks, we will implement a get_page function
    (prototype: def get_page(url: str) -> str:). The core of
    the function is very simple. It uses the requests module to
    obtain the HTML content of a particular URLand returns it.
"""

import requests
import redis


def get_page(url: str) -> str:
    """
        Automatically parametrize Cache.get
        with the correct conversion function.
    """
    cache = redis.Redis()
    key = f"count:{url}"

    cache.setex(key, 10, 0)
    cache.incr(key)

    return requests.get(url).text

if __name__ == '__main__':
    print(get_page('http://slowwly.robertomurray.co.uk'))
