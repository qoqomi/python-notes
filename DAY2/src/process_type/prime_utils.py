import random
import math

# 소수 판별 및 난수 생성 유틸 함수 모음


# ---------------------------------
# 소수 판별 함수
# ---------------------------------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


# ---------------------------------
# 난수 리스트 생성
# ---------------------------------
def generate_numbers(count: int, min_val: int, max_val: int) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(count)]
