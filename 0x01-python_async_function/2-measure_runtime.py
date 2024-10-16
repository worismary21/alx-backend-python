#!/usr/bin/env python3
import time
wait_n = __import__('1_concurrent_coroutines').wait_n
measure_time = __import__('2-measure_runtime').measure_time

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return the average time per wait_n call.

    Args:
    n (int): The number of times to run wait_n.
    max_delay (int): The maximum delay for wait_random.

    Returns:
    float: The average time per wait_n call.
    """
    start_time = time.time()  
    await wait_n(n, max_delay)  
    end_time = time.time() 
    
    total_time = end_time - start_time  
    return total_time 