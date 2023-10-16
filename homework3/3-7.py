def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# 输入两个正整数
num1 = int(input("请输入第一个正整数: "))
num2 = int(input("请输入第二个正整数: "))

# 调用手动实现的函数计算最大公约数
gcd = gcd_euclidean(num1, num2)

print(f"{num1} 和 {num2} 的最大公约数是 {gcd}")
