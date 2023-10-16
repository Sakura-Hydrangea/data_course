
import numpy as np
import math

N = 1000000
sum = 0
for i in range(N):
    x = np.random.uniform(2,3)
    sum += x**2 + 4*x*math.sin(x)
result = sum/N

print(result)