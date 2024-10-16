import asyncio
import time

# Dynamically import async_comprehension
async_comprehension = __import__('async_comprehension').async_comprehension 

async def measure_runtime():
    """Measure the runtime of async_comprehension executed four times in parallel."""
    start_time = time.time()  

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    total_time = time.time() - start_time  
    return total_time

# To run the coroutine
if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {runtime} seconds")
