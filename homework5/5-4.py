# 定义一个希尔排序的函数，接受一个列表和一个间隔序列作为参数
def shell_sort(lst, gaps):
  # 遍历间隔序列，从大到小
  for gap in gaps:
    # 对每个间隔，遍历列表
    for i in range(gap, len(lst)):
      # 将当前元素存储在temp中
      temp = lst[i]
      # 将当前元素之前的间隔元素的索引存储在j中
      j = i
      # 比较temp和间隔元素，如果temp小于某个间隔元素，就将该元素向右移动一位，为temp腾出空间
      # 如果想要降序排序，可以将temp < lst[j - gap]改为temp > lst[j - gap]
      while j >= gap and temp < lst[j - gap]:
        lst[j] = lst[j - gap]
        j -= gap
      # 将temp插入到正确的位置
      lst[j] = temp

lst = [9, 5, 1, 4, 3, 6, 7, 2, 8]
# 定义一个间隔序列，这里使用Shell原始序列
gaps = [4, 2, 1]
shell_sort(lst, gaps)
print(lst)

#关于希尔排序的时间复杂度和空间复杂度，它们都和间隔序列的选择有关。
# 一般来说，希尔排序的时间复杂度在最坏情况下是O (n^2)，在最好情况下是O (n)，在平均情况下是O (n^1.3)~O (n^1.5)。
# 希尔排序的空间复杂度是O (1)，因为它只需要一个额外的变量来存储当前元素。
