#!/usr/bin/env python3
'''
This module defines async_generator, a coroutine that yields random numbers.
'''

import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_generator():
    """An asynchronous generator that yields 10 random numbers after waiting 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)  
        yield random.uniform(0, 10) 