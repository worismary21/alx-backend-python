#!/usr/bin/env python3
'''
This module imports wait_random and defines task_wait_random
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates and returns an asyncio Task for the wait_random coroutine
    Args:
        max_delay (int): The maximum delay for wait_random
    Returns:
        asyncio.Task: A Task object that schedules the wait_random coroutine
    '''
    return asyncio.create_task(wait_random(max_delay))
