#!/usr/bin/env python3
"""
Module to fetch and cache web pages using Redis.
"""
import requests
import redis
from typing import Callable
from functools import wraps


# Initialize Redis client
r = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the result of a web page fetch and track access count.
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache the page and count accesses.
        """
        cache_key = f"count:{url}"
        r.incr(cache_key)
        cached_page = r.get(url)

        if cached_page:
            return cached_page.decode('utf-8')

        result = method(url)
        r.setex(url, 10, result)
        return result

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a particular URL and return it.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))  # Should return cached content
    print(r.get(f"count:{url}").decode('utf-8'))  # Should print the access count
