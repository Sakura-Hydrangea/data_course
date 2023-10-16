
input_string = input("请输入一个数字列表，用逗号或空格分隔每个数字： ")
number_list = [int(num) for num in input_string.split()]
for i in range(len(number_list) - 1, -1, -1):
    print(number_list[i])

index = len(number_list)-1
while index >= 0:
    print(number_list[index])
    index -= 1