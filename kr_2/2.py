import random
import time
from threading import Thread


s = [random.randint(0, 100000000) for i in range(10**6)]

if sum(s) % 2 == 0:
    print('true')
else:
    print('false')

# только это могу сделать блинб...