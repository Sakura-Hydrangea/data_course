import re


def validate_chinese_id_card(id_card):
    # 正则表达式模式匹配18位身份证号
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}(\d|X|x)$'

    if re.match(pattern, id_card):
        # 验证通过
        return True
    else:
        # 验证失败
        return False


# 输入要验证的身份证号
id_card = input("请输入18位身份证号: ")

if validate_chinese_id_card(id_card):
    print("身份证号合法")
else:
    print("身份证号不合法")

