# -*- coding: utf-8 -*- 
# sum a ~ b

print('sum a ~ b')
a = int(input('a : '))
b = int(input('b : '))

# a가 더 큰 경우, a와 b의 값을 교환
if a > b: a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print('sum : {}'.format(sum))