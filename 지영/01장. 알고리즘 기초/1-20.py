# 1~12까지 8을 건너뛰고 출력하기 2

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')

print()

# 1-19 예시보다 효율적이지만 for문은 생성한 리스트의 원소를 하나씩 꺼내 반복하므로 반복을 위한 연산 비용이 여전히 발생함