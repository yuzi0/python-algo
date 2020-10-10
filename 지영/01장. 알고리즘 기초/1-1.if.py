# -*- coding: utf-8 -*- 
# 세 정수를 입력받아 최대값 구하기

print("Get max num")
a = int(input("input a :"))
b = int(input("input b :"))
c = int(input("input c :"))

max = a
# 조건식 => 선택 구조
if b > max: max = b
if c > max: max = c

print('max : {}'.format(max))