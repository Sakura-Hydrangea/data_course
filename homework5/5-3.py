# 定义一个插入排序的函数，接受一个列表作为参数
def insertion_sort(lst):
  # 从第二个元素开始遍历列表
  for i in range(1, len(lst)):
    # 将当前元素存储在key中
    key = lst[i]
    # 将当前元素之前的已排序部分的最后一个元素的索引存储在j中
    j = i - 1
    # 比较key和已排序部分的元素，如果key小于某个元素，就将该元素向右移动一位，为key腾出空间
    # 如果想要降序排序，可以将key < lst[j]改为key > lst[j]
    while j >= 0 and key < lst[j]:
      lst[j + 1] = lst[j]
      j = j - 1
    # 将key插入到正确的位置
    lst[j + 1] = key

lst = [9, 5, 1, 4, 3]
insertion_sort(lst)
print(lst)
