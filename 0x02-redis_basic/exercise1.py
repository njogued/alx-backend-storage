#!/usr/bin/env python3
"""0. Cache class with init and store method
1. Byte to str or int"""
import redis
import uuid
from typing import Union, Callable, Optional
from functool import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a function is called"""

    key = method.__qualname__  # Get the qualified name of the method

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the count"""

        self._redis.incr(key)  # Increment the count using Redis
        return method(self, *args, **kwargs)  # Call the original method

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that stores the history of inputs and outputs of a function"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores inputs and outputs"""

        input = str(args)  # Convert input arguments to a string
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(fn: Callable):
    """Function that displays the history of calls for a particular function"""

    r = redis.Redis()  # Create a Redis client
    function_name = fn.__qualname__  # Get the qualified name of the function

    value = r.get(function_name)  # Get the count value from Redis
    try:
        value = int(value.decode("utf-8"))  # Convert the count value
    except Exception:
        value = 0

    print("{} was called {} times:".format(function_name, value))

    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")  # Convert input to a string
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")  # Convert output to a string
        except Exception:
            output = ""

        print("{}(*{}) -> {}".format(function_name, input, output))


class Cache:
    """Cache class to implement redis"""

    def __init__(self):
        """Create and store an instance of Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and return it"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """Function to convert the stored byte data to readable format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_int(self, key: str) -> int:
        """Decode the value returned from the get method"""
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8")
        except Exception:
            data=0
        return data

    def get_str(self, key: str) -> str:
        """Decode data to int"""
        data=self._redis.get(key)
        return data.decode("utf-8")
