# sum a ~ b
# 1-10을 개선한 코드

print('sum a ~ b')
a = int(input('a :'))
b = int(input('b :'))

if a > b: a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end = '')
    sum += i


# 마지막에 한번만 if문을 빼서 알고리즘 효율을 올림
print(f'{b} = ', end = '')
sum += b

print(sum)