#在n>4的情况下，将n尽可能划分出多的3，只剩下4的时候，分解式直接取4就是最大值
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

