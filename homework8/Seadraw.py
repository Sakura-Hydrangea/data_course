# 导入seaborn和matplotlib模块
import seaborn as sns
import matplotlib.pyplot as plt

# 定义数据集
x = [1, 2, 3, 4, 5, 6, 7] # 一周的时间
y = [100, 105, 102, 108, 110, 107, 111] # 股票价格

# 创建一个画布和三个子图
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# 在第一个子图上绘制折线图
sns.lineplot(x=x, y=y, ax=ax1)
ax1.set_xlabel("Time")
ax1.set_ylabel("Price")
ax1.set_title("Line plot")

# 在第二个子图上绘制柱状图
sns.barplot(x=x, y=y, ax=ax2)
ax2.set_xlabel("Time")
ax2.set_ylabel("Price")
ax2.set_title("Bar plot")

# 在第三个子图上绘制散点图
sns.scatterplot(x=x, y=y, ax=ax3)
ax3.set_xlabel("Time")
ax3.set_ylabel("Price")
ax3.set_title("Scatter plot")

# 显示图像
plt.show()
