"""
====================================
# 과제명: 단일 프로세스 vs 멀티 프로세스 성능 비교
# 작성자: 유승연 / 2077
# 작성일: 2025-09-17
# 설명:
  단일 프로세스와 멀티프로세스의 소수 판별 성능을 비교하는 프로그램
  1) 공통 숫자 리스트 생성
  2) 단일 프로세스로 소수 개수 계산 및 시간 측정
  3) 멀티프로세스로 소수 개수 계산 및 시간 측정
  4) 성능 비교 결과 출력
====================================
"""

import time
from .prime_utils import generate_numbers
from .single_process import single_process
from .multi_process import multi_process


def run_performance_comparison():
    """성능 비교 실행"""
    NUM_COUNT = 10_000_000
    MIN_VAL = 1
    MAX_VAL = 1_000_00

    print("=" * 50)
    print("단일 프로세스 vs 멀티프로세스 성능 비교")
    print("=" * 50)

    # 공통으로 사용할 숫자 리스트 생성
    print("\n=== 숫자 리스트 생성 중 ===")
    start_gen = time.time()
    numbers = generate_numbers(NUM_COUNT, MIN_VAL, MAX_VAL)
    gen_time = time.time() - start_gen
    print(f"Generated {len(numbers)} numbers in {gen_time:.2f} seconds")

    # 단일 프로세스 성능 측정
    print("\n=== 단일 프로세스 테스트 ===")
    single_count, single_time = single_process(numbers)
    print(f"Single Process: {single_count} primes found in {single_time:.2f} seconds")

    # 멀티프로세스 성능 측정
    print("\n=== 멀티프로세스 테스트 ===")
    multi_count, multi_time = multi_process(numbers)
    print(f"Multi Process: {multi_count} primes found in {multi_time:.2f} seconds")

    # 성능 비교 결과
    print("\n" + "=" * 50)
    print("성능 비교 결과")
    print("=" * 50)
    print(f"단일 프로세스: {single_time:.2f}초")
    print(f"멀티 프로세스: {multi_time:.2f}초")

    if multi_time > 0:
        speedup = single_time / multi_time
        print(f"속도 향상: {speedup:.2f}배")

        if speedup > 1:
            print("✅ 멀티프로세스가 더 빠름")
        elif speedup < 1:
            print("⚠️  단일 프로세스가 더 빠름")
        else:
            print("⚖️  성능이 동일함")

    print(f"소수 개수 일치: {'✅' if single_count == multi_count else '❌'}")

    if single_count != multi_count:
        print(f"  - 단일 프로세스: {single_count}개")
        print(f"  - 멀티프로세스: {multi_count}개")

    print("=" * 50)


def main():
    """메인 실행 함수"""
    try:
        run_performance_comparison()
    except KeyboardInterrupt:
        print("\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
