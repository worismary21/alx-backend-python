#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension
import 

async def async_comprehension():
    """Collects 10 random numbers using async comprehension from async_generator."""
    # Dynamically import async_generator
    async_generator = __import__('async_generator_module', fromlist=['async_generator']).async_generator

    # Use async comprehension to collect 10 random numbers
    random_numbers = [num async for num in async_generator()]
    return random_numbers