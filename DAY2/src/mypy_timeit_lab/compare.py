import timeit
import random
from no_type import square_sum as square_sum_no_type
from with_type import square_sum as square_sum_with_type


def main():
    print("=" * 50)
    print("제곱의 합 성능 비교 테스트")
    print("=" * 50)

    # 테스트 데이터 생성
    test_data = [random.randint(1, 100) for _ in range(100000)]  # 10만개
    print(f"테스트 데이터: {len(test_data)}개")

    # 성능 측정
    print("\n--- 성능 측정 ---")
    time_no_type = timeit.timeit(lambda: square_sum_no_type(test_data), number=1000)
    time_with_type = timeit.timeit(lambda: square_sum_with_type(test_data), number=1000)

    print(f"타입 힌트 없음: {time_no_type:.6f}초")
    print(f"타입 힌트 적용: {time_with_type:.6f}초")

    # 결과 검증
    result_no_type = square_sum_no_type(test_data)
    result_with_type = square_sum_with_type(test_data)
    print(f"\n결과: {result_no_type:,}")
    print(f"일치: {'✅' if result_no_type == result_with_type else '❌'}")

    # 성능 차이
    ratio = time_with_type / time_no_type
    print(f"\n성능 차이: {ratio:.2f}배")

    if ratio > 1.1:
        print("🔴 타입 힌트가 성능에 영향을 줍니다!")
    else:
        print("🟢 타입 힌트가 성능에 거의 영향을 주지 않습니다.")

    print("=" * 50)


if __name__ == "__main__":
    main()
