# sum 1 ~ n

print('sum 1 ~ n')
n = int(input('n :'))

sum = 0

# 반복 구조(루프) : 여러 조건이 성립하는 동안 반복해서 처리하는 것
for i in range(1, n): # 사전 판단 반복 구조 (실행하기 전에 반복을 계속할 것인지 판단)
    sum += i

print('sum : {}'.format(sum))