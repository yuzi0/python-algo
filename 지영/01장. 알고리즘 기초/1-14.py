# -*- coding: utf-8 -*- 
# *를 n개 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? '))
w = int(input('몇 개마다 줄바꿈할까요? '))

for i in range(n): # n번 반복
    print('*', end='')
    if i % n == w - 1: print()

if n % w: print()