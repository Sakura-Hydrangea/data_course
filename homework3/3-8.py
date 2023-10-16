import random
import time
import numpy as np
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

array = []
n = int(input())
for i in range(n+1):
    array.append(random.randint(1,100000))

start_selection = time.time()
selection_sort(array)
end_selection = time.time()
print(end_selection - start_selection)


start_merge = time.time()
merge_sort(array)
end_merge = time.time()
print(end_merge - start_merge)
# n = 1000 选择 0.014538764953613281秒 归并 0.0009992122650146484秒
# n = 10000 选择 1.0695292949676514秒 归并 0.010110616683959961秒
# n = 100000 选择 165.26123356819153秒 归并 0.12160515785217285秒
#可以看到归并排序的效率远远高于选择排序