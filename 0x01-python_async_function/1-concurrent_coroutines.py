#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

async def main():
    """Main function to test the wait_n coroutine."""
    n = 5        
    max_delay = 10 
    delays = await wait_n(n, max_delay)  
    print(delays) 

if __name__ == "__main__":
    asyncio.run(main())  