# 导入matplotlib.pyplot模块
import matplotlib.pyplot as plt

# 定义实验次数和基尼系数的列表
experiments = [1, 2, 3, 4, 5, 6]
gini = [0.44, 0.62, 0.43, 0.36, 0.88, 0.72]

# 使用plot函数画出折线图
plt.scatter(experiments,gini)
plt.plot(experiments, gini)

# 使用axhline函数在y=0.62处画出一条蓝色的虚线
plt.axhline(y=0.62, color='b', linestyle='--')

# 使用title函数添加标题
plt.title("Gini on every labs")

# 使用set_ylim ()函数设置y轴的范围为0到1
plt.ylim((0, 1))

# 使用xlabel函数和ylabel函数添加横轴和纵轴标签
plt.xlabel("lab")
plt.ylabel("Gini")

plt.show()
# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 创建数据框，第一列为年份，第二列为基尼系数
data = pd.DataFrame({'year': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], 'gini': [0.479, 0.473, 0.485, 0.487, 0.484, 0.491, 0.490, 0.481, 0.477, 0.474, 0.473, 0.469, 0.462, 0.465, 0.467, 0.468, 0.465]})

# 设置图形大小和标题
plt.figure(figsize=(10, 6))
plt.title('China Gini Coefficient from 2003 to 2019')

# 绘制折线图，横轴为年份，纵轴为基尼系数，设置颜色和标签
plt.plot(data['year'], data['gini'], color='blue', label='Gini Coefficient from government')
plt.scatter(data['year'], data['gini'], color='blue', label='Gini Coefficient from government')
plt.scatter(2011,0.61,color='green',label = 'Gini Coefficient from SUWFE')
plt.scatter(2012,0.73,color='red',label = "Gini Coefficient from BKU")

# 添加网格线和图例
plt.grid()
plt.legend()

# 显示图形
plt.show()



