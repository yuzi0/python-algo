# 세 정수의 최댓값 구하기

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    max = a
    if b > max: max = b
    if c > max: max = c
    return max



print('max3(1, 2, 3) : {}'.format(max3(1, 2, 3)))
print('max3(11, 21, 13) : {}'.format(max3(11, 21, 13)))