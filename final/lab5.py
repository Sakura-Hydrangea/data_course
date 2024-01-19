# 导入随机数，绘图和数学库
import random
import matplotlib.pyplot as plt
import numpy as np

# 创建一个长度为100的列表，表示100个人的初始财富，前90个元素的值为100，后10个元素的值为500，表示富二代玩家的初始财富
wealth = [100] * 90 + [500] * 10

# 定义一个函数，表示每轮游戏的过程，即每个人随机选择一个人，给他一美元，同时自己减少一美元
def play_game():
    global wealth # 使用全局变量
    for i in range(100): # 遍历列表中的每个元素
        j = random.randint(0, 99) # 随机选择一个索引，表示被选中的人
        if i >= 90 : #如果是富二代玩家输了
            wealth[i] -= 2  # 该玩家需要拿出2元
            wealth[j] += 2  # 被选中的玩家获得2元
        elif j >= 90: # 如果被选中的玩家是富二代
            wealth[i] -= 2 # 该玩家需要拿出2元
            wealth[j] += 2 # 被选中的玩家获得2元
            k = random.randint(0, 99) # 再随机选择一个索引，表示富二代的第二次机会
            if k == j: # 如果是同一个玩家
                wealth[i] -= 2 # 该玩家再拿出2元
                wealth[j] += 2 # 被选中的玩家再获得2元
        else: # 如果被选中的玩家是普通人
            wealth[i] -= 1 # 该玩家拿出1元
            wealth[j] += 1 # 被选中的玩家获得1元


# 使用for循环，重复执行17000次游戏函数，更新列表中的元素值，表示每个人的最终财富

for _ in range(17000):
    play_game()

# 对列表中的元素进行排序，使得财富值从小到大排列
rich_wealth = [wealth[i] for i in range(90,100)]
wealth_another = wealth
wealth_another = sorted(wealth_another)
print(rich_wealth)

# 使用numpy库，创建一个长度为100的数组，表示玩家的编号，从1到100
player = np.arange(1, 101)

# 使用matplotlib库，绘制一个柱状图，表示100个人的财富分布，横轴为玩家的编号，纵轴为财富值，用蓝色表示普通玩家，用红色表示富二代玩家
plt.bar(player, wealth_another, color=['red' if wealth_another[i] in rich_wealth else 'blue' for i in range(100)])
plt.xlabel('Player') # 设置横轴的标签
plt.ylabel('Wealth') # 设置纵轴的标签
plt.title('Wealth distribution of 100 people playing game') # 设置标题
plt.show() # 显示柱状图

#使用numpy库，创建一个长度为100的数组，表示人口比例，从0.01到1
population = np.arange(0.01, 1.01, 0.01)

# 使用numpy库，创建一个长度为100的数组，表示财富比例，即每个人的财富占总财富的百分比
wealth = np.array(wealth_another)
total_wealth = np.sum(wealth)
wealth_ratio = wealth / total_wealth

# 计算每组的人口占总人口的比例，这里假设每组的人口相等，你可以根据你的数据进行修改
population_ratio = np.full(len(wealth), 1 / len(wealth))

# 计算每组的累计收入或财富比例和累计人口比例
cumulative_wealth_ratio = np.cumsum(wealth_ratio)
cumulative_population_ratio = np.cumsum(population_ratio)

# 使用matplotlib库，绘制一个洛伦兹曲线，表示100个人的财富分布，横轴为人口比例，纵轴为财富比例
plt.plot(cumulative_population_ratio, cumulative_wealth_ratio, label="Lorenz curve")
plt.plot(population, population, '--', label="Perfect equality") # 设置对角线的参数和标签
plt.xlabel("Population ratio") # 设置横轴的标签
plt.ylabel("Wealth ratio") # 设置纵轴的标签
plt.title("Wealth distribution of 100 people playing game") # 设置标题
plt.legend() # 显示图例
plt.show() # 显示曲线图

# 定义一个函数，计算基尼系数，利用基尼系数的定义，计算数组中每两个元素的绝对差的平均值，然后除以数组的平均值，再乘以0.5
def gini(wealth):
    # 将数组排序
    wealth = sorted(wealth)
    # 计算数组的总和
    total = sum(wealth)
    # 初始化累积占比和人数的累积占比
    cum_wealth = 0
    cum_people = 0
    # 初始化占比乘积的和
    prod_sum = 0
    # 遍历数组中的每个元素
    for x in wealth:
        # 更新累积占比和人数的累积占比
        cum_wealth += x
        cum_people += 1
        # 更新占比乘积的和
        prod_sum += cum_wealth * cum_people / total
    # 计算基尼系数
    return 1 - 2 * prod_sum / (len(wealth) ** 2)


# 调用gini函数，传入财富数组，得到基尼系数的值
gini_coefficient = gini(wealth_another)

# 打印基尼系数的值
print("The Gini coefficient is:", gini_coefficient)

# 对财富列表进行降序排序
wealth_desc = sorted(wealth, reverse=True)

# 计算财富前10%的人所拥有的财产总数占所有人总财产的比例
top_10_wealth = sum(wealth_desc[:10]) # 取出前10个财富值，求和
top_10_ratio = top_10_wealth / total_wealth # 除以总财富，得到比例
print("The wealth ratio of the top 10% is:", top_10_ratio)

# 计算财富前20%的人所拥有的财产总数占所有人总财产的比例
top_20_wealth = sum(wealth_desc[:20]) # 取出前20个财富值，求和
top_20_ratio = top_20_wealth / total_wealth # 除以总财富，得到比例
print("The wealth ratio of the top 20% is:", top_20_ratio)

# 计算财产100元以下的人所占总人口的比例
below_100_num = len([w for w in wealth if w <= 100]) # 筛选出小于等于100的财富值，计算其个数
below_100_ratio = below_100_num / len(wealth) # 除以总人数，得到比例
print("The population ratio of the people with wealth below 100 is:", below_100_ratio)