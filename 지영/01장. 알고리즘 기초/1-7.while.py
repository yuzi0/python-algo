# sum 1 ~ n

print('sum 1 ~ n')
n = int(input('n :'))

sum = 0
i = 1 # 카운더용 변수

# 반복 구조(루프) : 여러 조건이 성립하는 동안 반복해서 처리하는 것
while i <= n: # 사전 판단 반복 구조 (실행하기 전에 반복을 계속할 것인지 판단)
    sum += i
    i += 1

print('sum : {}'.format(sum))