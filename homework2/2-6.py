
def cube_root():
    c = 10
    g = c / 2
    while (abs(g ** 3 - c) > 1e-10):
        g = g - (g ** 3-c)/(3*(g**2))
    print(g)
cube_root()