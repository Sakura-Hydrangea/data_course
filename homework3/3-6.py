score = int(input())

if score >= 90:
    print("优秀")
elif 75 <= score <= 89:
    print("良好")
elif 60 <= score <= 74:
    print("合格")
else:
    print("不合格")