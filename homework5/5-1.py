
import math


def is_prime(a):
  # 如果a小于等于1，返回False
  if a <= 1:
    return False
  # 如果a等于2，返回True
  if a == 2:
    return True
  # 从2到a的平方根之间遍历所有的数
  for i in range(2, int(math.sqrt(a)) + 1):
    # 如果a能被i整除，返回False
    if a % i == 0:
      return False
  # 如果没有找到能整除a的数，返回True
  return True

n = int(input())
print(is_prime(n))