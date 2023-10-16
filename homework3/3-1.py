decimal_number = float(input())

decimal_number_int = int(decimal_number)
binary_number = ""

#计算整数部分
def decimal_to_binary(decimal_integer):
    if decimal_integer == 0:
        return "0"

    binary_result = ""
    while decimal_integer > 0:
        # 每次取余数并将其添加到结果的开头
        remainder = decimal_integer % 2
        binary_result = str(remainder) + binary_result
        decimal_integer = decimal_integer // 2
    return binary_result+"."

#计算小数部分
while decimal_number != 0:
    decimal_number *= 2
    if decimal_number >= 1:
        binary_number += str(1)
    else:
        binary_number += str(0)
    decimal_number -= int(decimal_number)

print(decimal_to_binary(decimal_number_int)+binary_number)

