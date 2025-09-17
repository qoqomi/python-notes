"""
====================================
# 과제명: 직원(Employee) 데이터 필터링
# 작성자: 유승연 / 2077
# 작성일: 2025-09-16
# 설명:
  직원 리스트를 조건에 맞게 필터링 및 정렬하는 프로그램
  1) 부서가 Engineering이고 salary >= 80000인 직원 이름 출력
  2) 30세 이상 직원의 (name, department) 출력
  3) salary 기준 내림차순 정렬 후 상위 3명 (name, salary) 출력
  4) 모든 부서별 평균 급여를 출력
====================================
"""

# ---------------------------------
# 1) Engineering 부서 직원 중 salary >= 80000인 직원의 이름 리스트 반환
# ---------------------------------


def get_engineering_high_salary(employees):
    return [
        emp["name"]
        for emp in employees
        if emp["department"] == "Engineering" and emp["salary"] >= 80000
    ]


# ---------------------------------
# 2) 나이가 30세 이상인 직원의 (name, department) 튜플 리스트 반환
# ---------------------------------


def get_over_30(employees):
    """"""
    return [(emp["name"], emp["department"]) for emp in employees if emp["age"] >= 30]


# ---------------------------------
# 3) 급여 기준 내림차순으로 상위 3명의 (name, salary) 튜플 리스트 반환
# ---------------------------------
def get_top3_salary(employees):
    """"""
    sorted_employees = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
    return [(emp["name"], emp["salary"]) for emp in sorted_employees[:3]]


# -------------------------------------------------------------
# End of code
# -------------------------------------------------------------


def main():
    """메인 실행 함수"""
    employees = [
        {"name": "Alice", "department": "Engineering", "age": 30, "salary": 85000},
        {"name": "Bob", "department": "Marketing", "age": 25, "salary": 60000},
        {"name": "Charlie", "department": "Engineering", "age": 35, "salary": 95000},
        {"name": "David", "department": "HR", "age": 45, "salary": 70000},
        {"name": "Eve", "department": "Engineering", "age": 28, "salary": 78000},
    ]

    result1 = get_engineering_high_salary(employees)
    result2 = get_over_30(employees)
    result3 = get_top3_salary(employees)

    print(f"1) Engineering + salary >= 80000: {result1}")
    print(f"2) 30세 이상 직원: {result2}")
    print(f"3) 급여 Top 3: {result3}")


if __name__ == "__main__":
    main()
