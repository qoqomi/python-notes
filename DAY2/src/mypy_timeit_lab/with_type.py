"""
====================================
# 과제명: 타입 힌트를 적용한 함수들
# 작성자: 유승연 / 2077
# 작성일: 2025-09-17
# 설명:
  타입 힌트를 적용한 함수들
====================================
"""

# 타입 힌트를 적용한 함수들

from typing import List


def square_sum(nums: List[int]) -> int:
    """정수 리스트의 각 원소 제곱의 합 (타입 힌트 + Duck Typing 적용)"""
    # Duck Typing: try-except로 타입 안전성 확보
    try:
        result: int = 0
        for x in nums:
            # Duck Typing: * 연산이 가능한지 확인
            result += x * x
        return result
    except (TypeError, AttributeError) as e:
        raise TypeError(f"Invalid input type: {e}")


def square_sum_list_comprehension(nums: List[int]) -> int:
    """정수 리스트의 각 원소 제곱의 합 - 리스트 컴프리헨션 (타입 힌트 + Duck Typing 적용)"""
    # Duck Typing: try-except로 타입 안전성 확보
    try:
        return sum(x * x for x in nums)
    except (TypeError, AttributeError) as e:
        raise TypeError(f"Invalid input type: {e}")


def square_sum_map(nums: List[int]) -> int:
    """정수 리스트의 각 원소 제곱의 합 - map 사용 (타입 힌트 + Duck Typing 적용)"""
    # Duck Typing: try-except로 타입 안전성 확보
    try:
        return sum(map(lambda x: x * x, nums))
    except (TypeError, AttributeError) as e:
        raise TypeError(f"Invalid input type: {e}")
