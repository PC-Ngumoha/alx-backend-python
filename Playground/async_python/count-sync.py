#!/usr/bin/env python3
import time

def count():
  print('One')
  time.sleep(1)
  print('two')

def main():
  for _ in range(3):
    count()

if __name__ == '__main__':
  startTime = time.perf_counter()
  main()
  elapsedTime = time.perf_counter() - startTime
  print(f'{__file__} executed in {elapsedTime:.2f} seconds')
