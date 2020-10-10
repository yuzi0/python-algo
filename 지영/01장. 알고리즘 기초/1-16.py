# -*- coding: utf-8 -*- 
# Sum 1 ~ n (양수만 입력받음)

while True: # 무한 루트(infinite loop)
    n = int(input('몇 개를 출력할까요? '))
    if n > 0: break # n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i # sum에 i를 더함
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')