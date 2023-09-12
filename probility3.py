import numpy as np
import math
#J1平均值法
time = 100000
sum = 0
for i in range(time):
    x = np.random.uniform(0, 1)
    sum += (math.exp(x)-1)/(math.exp(1)-1)
print(sum/time)
#J1随机投点法
sum = 0
for i in range(time):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if y<(math.exp(x)-1)/(math.exp(1)-1):
        sum+=1
print(sum/time)
#J2平均值法
sum = 0
for i in range(time):
    x = np.random.uniform(-1.1)
    sum+=math.exp(x)
print(2*sum/time)
#J2随机投点法
sum = 0
for i in range(time):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if y<(math.exp(x)+math.exp(-x))/(math.exp(1)+math.exp(-1)):
        sum+=1
print((sum/time)*(math.exp(1)+math.exp(-1)))