#!/usr/bin/env python
from time import time as tme
# create variable
nemo = ['nemo' for i in range(10)]

def findnemo(arr):
  t0 = tme
  print(f'array = {arr[0]}')
  print(f'array = {arr[1]}')
  t1= tme
  print(f'time taken = {t1-t0}')


findnemo(nemo)