#!/usr/bin/python3
"""
    In this tasks, we will implement a get_page function
    (prototype: def get_page(url: str) -> str:). The core of
    the function is very simple. It uses the requests module to
    obtain the HTML content of a particular URLand returns it.
"""

import requests


def get_page(url: str) -> str:
    """
        Automatically parametrize Cache.get
        with the correct conversion function.
    """
    return requests.get(url).text
