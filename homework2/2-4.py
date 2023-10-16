def square_root():
    c = 2
    g = 1   #g为平方根
    #误差设置为1e-6,步长为1e-7
    while(abs(g * g - c) > 0.000001):
        g += 0.0000001
    print(g)


square_root()