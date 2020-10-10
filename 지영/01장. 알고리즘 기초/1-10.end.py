# sum a ~ b

print('sum a ~ b')
a = int(input('a :'))
b = int(input('b :'))

if a > b: a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b: print(f'{i} + ', end = '')
    else: print(f'{i} = ', end = '')
    sum += i

print(sum)