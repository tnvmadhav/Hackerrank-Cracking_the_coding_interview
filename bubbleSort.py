#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def bubblesort(array):
    count = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                count += 1
                array[j], array[j+1] = array[j+1], array[j]
    print("Array is sorted in %d swaps."% count)
    print("First Element: %d"% array[0])
    print("Last Element: %d"% array[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    bubblesort(a)
