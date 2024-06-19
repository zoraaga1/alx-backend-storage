#!/usr/bin/env python3
"""
Module for task 0
"""

from redis import Redis
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
  """
  Class Cache
  """

  def __init__(self):
    """
    Initialize class
    """
    self._redis = Redis()
    self._redis.flushdb()

  def store(self, data: Union[str, bytes, int, float]) -> str:
    """
    Store data
    """
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key
