import random
import time
#1.蒙特卡洛方法
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5<=1:
            inCircle += 1
    return 4*(inCircle/numNeedles)

n = 10000
start_1 = time.time()
result_pi_1 = throwNeedles(n)
end_1 = time.time()
print("蒙特卡洛方法:" "{:.10f}".format(result_pi_1))

#2.莱布尼茨级数 pi = 4(Σ(-1)**i+ * (2*i+1))
def leibniz(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i / (2*i+1)
    return 4 * pi

n = 10000
start_2 = time.time()
result_pi_2 = leibniz(n)
end_2 = time.time()
print("莱布尼茨级数：" "{:.10f}".format(result_pi_2))

# 3.BBP公式法
def bbp(n):
    pi = 0
    for k in range(n):
        pi += 1/pow(16, k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    return pi

n = 100000
start_3 = time.time()
result_pi_3 = bbp(n)
end_3 = time.time()
print("公式法:" "{:.10f}".format(result_pi_3))

print("蒙特卡洛用时：" "{:}".format(end_1 - start_1))
print("莱布尼茨用时：" "{:}".format(end_2 - start_2))
print("公式法用时：" "{:}".format(end_3 - start_3))
#结果可以发现 蒙特卡洛法的用时是最短的，但由于因为其随机模拟，所以每一次pi的求值都不一样，且精度也比较低
#而莱布尼茨和bbp公式法的精度比起蒙特卡洛的精度要好得多，但公式法的用时较大，n到100000就需要30秒了，因此效率较低
