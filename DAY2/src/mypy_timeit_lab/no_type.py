# no_type.py
# 타입 힌트를 사용하지 않은 함수들


def square_sum(nums):
    """정수 리스트의 각 원소 제곱의 합 (타입 힌트 없음)"""
    result = 0

    for x in nums:
        result += x * x
    return result


def square_sum_list_comprehension(nums):
    """정수 리스트의 각 원소 제곱의 합 - 리스트 컴프리헨션 (타입 힌트 없음)"""
    return sum(x * x for x in nums)


def square_sum_map(nums):
    """정수 리스트의 각 원소 제곱의 합 - map 사용 (타입 힌트 없음)"""
    return sum(map(lambda x: x * x, nums))
