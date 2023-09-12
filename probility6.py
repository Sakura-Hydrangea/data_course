import scipy
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#情况1 方差为3，样本量为10
alpha = 0.05
for i in range(100):
    n = 10
    samples = stats.norm.rvs(0,3,size=n)
    average = np.average(samples)
    std = 3
    left = average - scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    right = average + scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    region = (left,right)
    plt.plot([0,100],[0,0],color = 'black')
    plt.vlines(i,left,right)
plt.show()

#情况2 方差为3，样本量为100
alpha = 0.05
for i in range(100):
    n = 100
    samples = stats.norm.rvs(0,3,size=n)
    average = np.average(samples)
    std = 3
    left = average - scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    right = average + scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    region = (left,right)
    plt.plot([0,100],[0,0],color = 'black')
    plt.vlines(i,left,right)
plt.show()

#情况3 方差未知，样本量为10
alpha = 0.05
for i in range(100):
    n = 10
    samples = stats.norm.rvs(0,3,size=n)
    average = np.average(samples)
    std = np.std(samples)
    left = average - scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    right = average + scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    region = (left,right)
    plt.plot([0,100],[0,0],color = 'black')
    plt.vlines(i,left,right)
plt.show()

#情况4 方差未知，样本量为100
alpha = 0.05
for i in range(100):
    n = 100
    samples = stats.norm.rvs(0,3,size=n)
    average = np.average(samples)
    std = np.std(samples)
    left = average - scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    right = average + scipy.stats.t.ppf(1 - alpha / 2, n - 1) * std / (n ** 0.5)
    region = (left,right)
    plt.plot([0,100],[0,0],color = 'black')
    plt.vlines(i,left,right)
plt.show()

