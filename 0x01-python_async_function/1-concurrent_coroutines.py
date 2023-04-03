#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List
from random import randint


async def wait_random(max_delay: int) -> float:
    '''Waits for a random delay and returns it.
    '''
    delay = randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(wait_times)
