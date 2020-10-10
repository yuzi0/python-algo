# 직각 이등변 삼각형 2

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요 : '))

for i in range(n)):
    for _ in range(n - i - 1):  # 카운터용 변수로 _(언더 스코어) 사용
        print(' ', end='') # 공백 출력
    for _ in range(i + 1):
        print('*', end='') # * 출력
    print()