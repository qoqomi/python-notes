# 타입 힌트 + 정적 타입 검사 + 성능 측정 실습

## 내용 이해

1. `mypy`란?

- Python의 저적 타입 검사기(static type checker)
- 코드 실행 전에 타입 힌트가 올바른지 검사해준다.
- 런타임 성능에는 영향을 주지 않고, 개발 단계에서 오류를 미리 잡아준다.

```python
from typing import List

def square_sum()->int:
    return sum(x * x for x in num)

result = square_sum([1,2,3]) # OK
result2 = square_sum(["a","b"]) # 타입 불일치
```

➡️ 실행은 되지만, mypy를 돌리면 경고 발생:

```bash
$ mypy example.py
error: List item 0 has incompatible type "str"; expected "int"
```

2. ` timeit`이란?

- Python 표준 라이브러리 모듈 => 코드 실행 시간을 정확히 측정할 수 있음.
- 단순히 `time.time()`으로 재는 것보다 오차가 적고, 반복 실행으로 신뢰성 높은 결과 제공.

```python
import timeit

code = """
def square_sum(nums):
    return sum(x*x for x in nums)

square_sum(list(range(1000)))
"""

print(timeit.timeit(stmt=code, number=10000))

```

➡️ number=10000번 실행해서 걸린 총 시간을 반환.

### 정리

mypy: 정적 타입 검사 도구 → 코드 실행 전 타입 오류 확인 (개발 안정성 ↑)

timeit: 성능 측정 도구 → 코드 실행 시간을 정확하게 측정 (성능 비교 가능)

## 실습

- Python에서 **타입 힌트(Type Hint)** 사용 여부에 따른 차이를 이해하고,
- **mypy**를 활용한 정적 타입 검사,
- **timeit**을 활용한 실행 성능 비교를 수행한다.

### 요구사항

1. 정수 리스트를 입력받아 각 원소의 제곱을 합산하는 함수 작성
   - **A 버전**: 타입 힌트 미사용
   - **B 버전**: 타입 힌트 적용
2. `mypy`를 이용해 B 버전의 타입을 검사하고 결과 확인
3. `timeit`을 사용하여 두 버전의 실행 성능을 각각 측정하고 비교

### 폴더 구조

```bash
typehint_lab/
├─ no_type.py # A 버전 (타입 힌트 없음)
├─ with_type.py # B 버전 (타입 힌트 적용)
├─ compare.py # timeit으로 성능 비교 실행
└─ README.md # 실습 보고서
```

## 결론

mypy를 통해 타입 안정성을 확보할 수 있다.

timeit으로 확인한 결과, 타입 힌트의 유무는 실행 성능에 큰 차이가 없다.

따라서 타입 힌트는 성능보다는 코드 품질과 유지보수성 향상을 위해 사용해야 한다.
