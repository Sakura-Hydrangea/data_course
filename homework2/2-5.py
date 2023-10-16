c = int(input())
def square_root_1(c):
    g = c/2
    while(abs(g*g-c)>1e-10):
        g = (g+c/g)/2
    print(g)

def square_root_2(c):
    g = c
    while(abs(g*g-c)>1e-10):
        g = (g+c/g)/2
    print(g)

def square_root_3(c):
    g = c/4
    while(abs(g*g-c)>1e-10):
        g = (g+c/g)/2
    print(g)
square_root_1(c)
square_root_2(c)
square_root_3(c)
# 以上三个函数根号2的结果分别为：
# 1.4142135623746899
# 1.4142135623746899
# 1.414213562373095
# 以上三个函数根号2000的结果分别为：
44.721359549995796
44.721359549995796
44.721359549995796

#可以发现，对精度有一定影响，但影响很小