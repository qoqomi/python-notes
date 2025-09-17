"""
====================================
# 과제명: 제너레이터 기반 메모리 절약형 로직 작성
# 작성자: 유승연 / 2077
# 작성일: 2025-09-16
# 설명:
  100만 개의 숫자 리스트를 처리하는 프로그램
  일반 리스트 방식은 메모리 과부하 발생 가능
  이를 해결하기 위해 제너레이터 기반 반복 구조를 직접 구현

  1) 아래 조건을 만족하는 제너레이터 함수 even_square_gen(n)을 작성할 것
     - 0 이상 n 미만의 정수 중 짝수만 제곱해서 하나씩 생성 (yield)
  2) 해당 제너레이터를 이용해 0부터 1,000,000까지의 짝수 제곱 총합을 계산
  3) 이 때의 메모리 사용량과 처리 속도를 비교 (time 모듈 활용)
====================================
"""

import sys
import time


# ---------------------------------
# 1) 제너레이터 함수
# ---------------------------------
def even_square_gen(n=1_000_000):
    for i in range(n):
        if i % 2 == 0:
            yield i**2


# ---------------------------------
# 2) 리스트 방식
# ---------------------------------
def list_sum_and_memory(n=1_000_000):
    start = time.time()
    numbers_list = [i**2 for i in range(n) if i % 2 == 0]  # 짝수만 제곱
    total = sum(numbers_list)
    elapsed = time.time() - start
    memory = sys.getsizeof(numbers_list)
    return total, memory, elapsed


# ---------------------------------
# 3) 제너레이터 방식
# ---------------------------------
def generator_sum_and_memory(n=1_000_000):
    start = time.time()
    numbers_generator = even_square_gen(n)
    total = sum(numbers_generator)
    elapsed = time.time() - start
    memory = sys.getsizeof(numbers_generator)
    return total, memory, elapsed


# -------------------------------------------------------------
# End of code
# -------------------------------------------------------------
def main():
    # 리스트 방식
    list_total, list_mem, list_time = list_sum_and_memory()
    print(f"[리스트 방식] 총합: {list_total}")
    print(f"[리스트 방식] 메모리 사용량: {list_mem} bytes")
    print(f"[리스트 방식] 처리 시간: {list_time:.5f} 초\n")

    # 제너레이터 방식
    gen_total, gen_mem, gen_time = generator_sum_and_memory()
    print(f"[제너레이터 방식] 총합: {gen_total}")
    print(f"[제너레이터 방식] 메모리 사용량: {gen_mem} bytes")
    print(f"[제너레이터 방식] 처리 시간: {gen_time:.5f} 초")


if __name__ == "__main__":
    main()
