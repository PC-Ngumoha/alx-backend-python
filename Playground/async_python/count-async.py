#!/usr/bin/env python3
import asyncio

async def count():
  print('One')
  await asyncio.sleep(1)
  print('Two')

async def main():
  await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
  import time
  startTime = time.perf_counter()
  asyncio.run(main())
  elapsedTime = time.perf_counter() - startTime
  print(f'{__file__} executed in {elapsedTime:.2f} seconds')
