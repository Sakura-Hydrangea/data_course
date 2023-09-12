import numpy as np
import scipy.stats as stats

# 定义样本量和p分位数的列表
sample_sizes = list(range(3, 21))
percentiles = [0.001, 0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.975, 0.99, 0.999]

# 初始化结果表格
skewness_table = np.zeros((len(percentiles), len(sample_sizes)))
kurtosis_table = np.zeros((len(percentiles), len(sample_sizes)))

# 执行蒙特卡洛模拟
np.random.seed(0)  # 设置随机种子以确保可重复性
for i, n in enumerate(sample_sizes):
    samples = np.random.standard_normal((10_000, n))  # 生成10,000个来自标准正态分布的样本
    sample_skewness = stats.skew(samples, axis=1)  # 计算样本偏度
    sample_kurtosis = stats.kurtosis(samples, axis=1)  # 计算样本峰度
    skewness_table[:, i] = np.percentile(sample_skewness, percentiles)  # 计算样本偏度的蒙特卡洛分布的各个p分位数
    kurtosis_table[:, i] = np.percentile(sample_kurtosis, percentiles)  # 计算样本峰度的蒙特卡洛分布的各个p分位数

# 打印样本偏度表格
print("Sample Skewness Monte Carlo Distribution:")
print("     ", end="")
for n in sample_sizes:
    print(f"  n={n:2d} ", end="")
print()
for i, p in enumerate(percentiles):
    print(f"p={p:.3f}", end="")
    for j in range(len(sample_sizes)):
        print(f"  {skewness_table[i, j]:.4f}", end="")
    print()

print()

# 打印样本峰度表格
print("Sample Kurtosis Monte Carlo Distribution:")
print("     ", end="")
for n in sample_sizes:
    print(f"  n={n:2d} ", end="")
print()
for i, p in enumerate(percentiles):
    print(f"p={p:.3f}", end="")
    for j in range(len(sample_sizes)):
        print(f"  {kurtosis_table[i, j]:.4f}", end="")
    print()