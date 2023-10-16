title = "数据科学与工程导论"
star = chr(0x2605)  # 使用Unicode代码点来获取星星字符

# 计算需要打印的星星的数量，以使其完全包围标题
padding_length = (40 - len(title)) // 2

# 打印上边的星星行
print(star * 40)

# 打印标题及其两侧的星星填充
print(star * padding_length + title + star * padding_length)

# 打印下边的星星行
print(star * 40)