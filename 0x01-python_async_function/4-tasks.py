#!/usr/bin/env python3
'''
This module defines task_wait_n, which schedules task_wait_random n times.
'''

import asyncio
from typing import List

# Import task_wait_random from the previous task
task_wait_random = __import__('2-measure_runtime').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Schedules task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of tasks to schedule.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of the delays in ascending order.
    '''
    # Create a list of asyncio Tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Await all tasks and gather results
    delays = await asyncio.gather(*tasks)

    # Return delays sorted in ascending order
    return sorted(delays)
