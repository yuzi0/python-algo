# 입력받은 정수의 부호는?

def sign(a):
    if a > 0: return "+"
    elif a < 0: return "-"
    else: return 0

n = int(input("num : "))
print("result : {}".format(sign(n)))