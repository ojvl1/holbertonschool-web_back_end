#!/usr/bin/env python3
'''
    import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather

    measure_runtime should measure the total runtime and return it.
'''
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
        Coroutine measure_runtime that will execute async_comprehension 4
        times in parallel using asyncio.gather. measure_runtime should
        measure the total runtime and return it.
    '''
    start = time.time()

    tasks = [(async_comprehension()) for _ in range(0, 4)]

    await asyncio.gather(*tasks)

    end = time.time()
    return end - start
