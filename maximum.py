#!/usr/bin/env python3

# Maximum algorithm 
# By: correodefinitivo97@gmail.com

import sys
import random

n = 100

data = []

for x in range(100):
    random_number = random.random
    data.append(random_number)

print(data)

maximum = -sys.float_info.max
for x in data:
    if x > maximum:
        maximum = x
    #print(x)

print(maximum)