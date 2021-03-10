import numpy as np

from random import *
a = [randint(1,8) for x in range(5)]

print('scegli un numero tra i seguenti ', a)

num = int(input())

rip = 0
for x in a:
    if x == num:
        rip = rip + 1
print('il numero scelto si ripete ', rip, ' volte')
