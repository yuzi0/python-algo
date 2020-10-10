# +, -를 번갈아 출력

print('print +-+-+-...')
n = int(input('how many?'))

for i in range(n):
    if i % 2: print('-', end = '')
    else: print('+', end = '')

print()