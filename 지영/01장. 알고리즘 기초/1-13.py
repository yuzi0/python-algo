# +, -를 번갈아 출력

print('print +-+-+-...')
n = int(input('how many?'))

for i in range(n // 2): print('+-', end = '')

if n % 2: print(f'+', end = '')

print()