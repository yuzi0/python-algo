class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # 2진수로 변환했을 때, 1의 갯수
        def bitCount(n: int) -> int:
            if n == 0: return 0
            return n % 2 + bitCount(n/2)

        # 소수 판별
        def primeNumber(n: int) -> int:
            if n != 1:
                for i in range(2, n):  
                    if n % i == 0: return False
            else: return False
            return True

        result = 0
        for n in range(L, R+1):
            if primeNumber(bitCount(n)):
                result += 1
        return result