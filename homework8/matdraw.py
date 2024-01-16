# 导入matplotlib模块
import matplotlib.pyplot as plt

# 生成一组二维数据集，x是时间，y是股票价格
x = [1, 2, 3, 4, 5, 6, 7] # 一周的时间
y = [100, 105, 102, 108, 110, 107, 111] # 股票价格

#用matplotlib绘制折线图
plt.plot(x, y) # 绘制折线
plt.scatter(x, y) # 绘制数据点
plt.xlabel("Time") # 设置x轴标签
plt.ylabel("Price") # 设置y轴标签
plt.title("Stock Price Change") # 设置标题
plt.show() # 显示图像


# 用matplotlib绘制散点图
plt.scatter(x, y) # 绘制数据点
plt.xlabel("Time") # 设置x轴标签
plt.ylabel("Price") # 设置y轴标签
plt.title("Stock Price Change") # 设置标题
plt.show() # 显示图像

# 用matplotlib绘制柱状图
plt.bar(x, y) # 绘制柱体
plt.xlabel("Time") # 设置x轴标签
plt.ylabel("Price") # 设置y轴标签
plt.title("Stock Price Change") # 设置标题
plt.show() # 显示图像


