
def has_repeated_chars(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

input_string = input()
if has_repeated_chars(input_string):
    print("字符串包含由两个或两个以上连续出现的相同字符组成的字符串。")
else:
    print("字符串不包含由两个或两个以上连续出现的相同字符组成的字符串。")