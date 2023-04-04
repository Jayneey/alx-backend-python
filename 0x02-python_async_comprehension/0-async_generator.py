#!/usr/bin/env python3
'''Task 0's module.
'''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())

