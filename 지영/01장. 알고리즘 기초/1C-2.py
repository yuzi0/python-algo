# 세 정수를 입력받아 중앙값 구하기

def mid3(a, b, c):
    if a >= b:
        if c >= a: return a
        elif b >= c: return b
        else: return c
    elif c > b: return b
    elif a > c: return a
    else: return c


print("Get mid num")

a = int(input("input a :"))
b = int(input("input b :"))
c = int(input("input c :"))

print('mid : {}'.format(mid3(a,b,c)))