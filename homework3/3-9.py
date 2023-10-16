A = []
B = []

n = int(input())
for i in range(n):
    x = int(input())
    A.append(x)
print(A)

for i in range(n):
    data = 1
    for j in range(n):
        if j!=i:
            data *= A[j]
    B.append(data)
print(B)