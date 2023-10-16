#1.若n=2001,所求的正整数列为677*3

#2.由数论的知识可以知道，拆分的数更接近自然对数，乘积越大，因此在n>4的情况下，将n尽可能划分出多的3
#余数为0，则全为3
#余数为2，则取两个2，其余为3
#余数为1的时候，分解式直接取一个2，剩下均为3
def max_product_partition(n):
    # 处理特殊情况
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n == 3:
        return [3]

    result = []

    while n > 4:
        result.append(3)
        n -= 3

    result.append(n)

    return result


# 测试
n = int(input())
print(max_product_partition(n))

