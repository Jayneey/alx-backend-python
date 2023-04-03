#!/usr/bin/env python3
'''Task 0's module
'''

import random
import asyncio

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

