import time
from .prime_utils import generate_numbers, is_prime


def single_process(numbers):
    """단일 프로세스로 소수 개수를 세는 함수"""
    start_time = time.time()

    # 소수 개수 세기
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1

    end_time = time.time()
    elapsed = end_time - start_time

    return prime_count, elapsed
