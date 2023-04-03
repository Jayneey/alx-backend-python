#!/usr/bin/env python3
'''Task 2's module.
'''
import time
from typing import List
from asyncio import run
from random import randint
from asyncio_tasks import wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n.
    '''
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == '__main__':
    n = 5
    max_delay = 10
    avg_time = measure_time(n, max_delay)
    print(f'Average time to execute wait_n({n}, {max_delay}): {avg_time:.2f} seconds')
