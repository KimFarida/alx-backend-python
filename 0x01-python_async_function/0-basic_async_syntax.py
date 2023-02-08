#!/usr/bin/env python3
"""Task 0 Module"""

import asyncio
import random

async def wait_random(max_delay: int = 10) ->float:
    """Waits for a random number in the range of max_delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
