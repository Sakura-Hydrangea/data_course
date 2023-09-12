from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import math
#求分位数
ppf_list = norm.ppf(q=[0.01, 0.025, 0.5, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 0.975, 0.99], loc=0, scale=1)
for i in range(17):
    print("%.6f" % ppf_list[i], end=" ")
#利用均匀分布生成正态分布，绘制直方图和密度函数图
list = []
for i in range(1000000):
    x = np.random.uniform()
    y = np.random.uniform()
    a_value = (-2*math.log(x))**(1.0/2)*math.cos(2*math.pi*y)
    list.append(a_value)
fig = plt.figure()
ax = fig.add_subplot()
ax.hist(list, bins=50, color='blue', density=True, alpha=0.7)
m = np.arange(-4, 4, 0.001)
n = (1 / np.sqrt(2 * math.pi)) * np.exp(-1 * pow(m, 2) / 2)
plt.plot(m, n, color = "red")
plt.title("标准正态分布伪随机数频率分布直方图和密度函数图")
plt.xlabel("伪随机数")
plt.ylabel("频率/组距")
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
