import random
n1 = 432
n2 = 232
n3 = 334
n = 1000
def fun_n11(p,q):
    return n1*p*q/(p*q+(1-p)*q*q)
def fun_n12(p,q):
    return n1*(1-p)*q*q/(p*q+(1-p)*q*q)
def fun_n21(p,q):
    return n2*p*(1-q)/(p*(1-q)+(1-p)*(1-q)*(1-q))
def fun_n22(p,q):
    return n2*(1-p)*(1-q)*(1-q)/(p*(1-q)+(1-p)*(1-q)*(1-q))
p = random.random()
q = random.random()
new_p = p
new_q = q
while True:
    p = new_p
    q = new_q
    n11 = fun_n11(p, q)
    n12 = fun_n12(p, q)
    n21 = fun_n21(p, q)
    n22 = fun_n22(p, q)
    new_p = (n11+n21)/n
    new_q = (n11+2*n12+n3)/(n+n12+n22+n3)
    if abs(new_p-p)<0.000001 and abs(new_q-q)<0.000001:
        p = new_p
        q = new_q
        break
print(p,q)