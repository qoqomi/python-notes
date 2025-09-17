"""
====================================
# 과제명: 제너레이터 기반 메모리 절약형 로직 작성
# 작성자: 유승연 / 2077
# 작성일: 2025-09-16
# 설명:
  100만 개의 숫자 리스트를 처리하는 프로그램
  일반 리스트 방식은 메모리 과부하 발생 가능
  이를 해결하기 위해 제너레이터 기반 반복 구조를 직접 구현

  1) 0부터 999,999까지의 정수를 담는 리스트를 생성하고 총합 구하기.
  2) 같은 결과를 제너레이터 함수로 구현.
  3) 두 방법의 메모리 사용 차이를 sys.getsizeof()로 확인.
====================================
"""

import sys


# ---------------------------------
# 1) 리스트 방식
# ---------------------------------


def list_sum_and_memory(n=1_000_000):
    numbers_list = [i for i in range(n)]
    list_sum = sum(numbers_list)
    list_memory = sys.getsizeof(numbers_list)
    return list_sum, list_memory


# ---------------------------------
# 2) 제너레이터 방식
# ---------------------------------


def generator_sum_and_memory(n=1_000_000):
    numbers_generator = (i for i in range(n))
    generator_sum = sum(numbers_generator)
    generator_memory = sys.getsizeof(numbers_generator)
    return generator_sum, generator_memory


# -------------------------------------------------------------
# End of code
# -------------------------------------------------------------


def main():
    list_sum, list_memory = list_sum_and_memory()
    generator_sum, generator_memory = generator_sum_and_memory()
    print(f"리스트 방식 총합: {list_sum}")
    print(f"제너레이터 방식 총합: {generator_sum}")
    print(f"리스트 방식 메모리: {list_memory}")
    print(f"제너레이터 방식 메모리: {generator_memory}")


if __name__ == "__main__":
    main()
