# dataclass(데이터 클래스)

```python
from dataclasses import dataclass
```

한번 지정하면 변경도 가능하다.

빠른 프로토타입 작성 시 유리하고 불변 속성 정의 시 @dataclass(frozen=True)가능

order =True

정렬이나 최적화를 하고 싶으면 불변으로 쓸 때 init

# slots(메모리 최적화)

## 개념

인스턴스가 가질 수 있는 속성 제한
**dict**미사용 -> 메모리 사용량 절감

## 비고

수많은 객체가 생성되는 환경에서 메모리 사용 효율화 대신 유연성은 떨어짐(동적 속성 추가 불가)

slot을 쓰게 되면 메모리 최적화가 가능하지만 동적 변화가 다르다 .

일반 클래스의 경우:

```python
class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


normal = Normal(1, 2)
normal.z = 3  # 문제없이 동작
print(normal.z)  # 3
```

**slots**를 사용한 클래스:

```python
class Optimized:
    __slots__ = ('x', 'y')  # x, y만 허용

    def __init__(self, x, y):
        self.x = x
        self.y = y

opt = Optimized(1, 2)
opt.z = 3  # ❌ AttributeError: 'Optimized' object has no attribute 'z'
```

백테를 이용하는 경우에는 컨테이너나 도커나 효율적으로 돌아가도록 하기 위해서 python에서 메모리 처리 속도가 중요함
벡터 값을 나오도록 하는 게 중요함

---

## 파일 읽기 / 쓰기

```python
# 파일 열기
file = open("example.txt","w")
# 파일에 쓰기
file.write()
file.write()
# 파일 닫기(반드시 닫아야 함)
# file.close()
```

## 데코레이터와 클로저 - 데코레이터

d2 = d2(say_hello)
d1 = d1(d2)

코드의 재사용성과 가독성 향성에 도움을 준다.

### 간단한 Decorator 예제

Decorator

## Global Inter Lock(GIL)

Python의 인터프리터에서 동시 실행을 제한하는 상태 관리 메커니즘으로 multithreading과 관련된 중요한 개념

## threading 모듈

- 장점: 메모리 공유, 생성 빠름
- 단점: GIL로 인해 CPU-bound 작업에 비효율

### 개념

하나의 프로세스 내에서 여러 스레드를 사용하여 병렬적으로 작업을 처리하는 기법
스레드는 프로세스 내에서 실행되는 흐름으로 하나의 프로세스에서 여러 스레드가 동시에 실행 가능

### 특징

스레드는 같은 프로세스를 공유하므로 메모리와 자원을 공유
multithreading은 주로 I/O 작업에 유리

```python
import threading


```

## Multiprocessing

### 개념

여러 개의 프로세스를 사용하여 작업을 병렬 처리하는 기법
각각의 프로세스는 독립된 메모리 공간과 자원을 갖고 실행
CPU 집약적인 작업에 적합

### 특징

각 프로세스는 별도의 메모리 공간을 갖기 때문에, 서로 영향을 미치지 않음
병렬 처리가 가능하여 CPU성능을 활용

### 종류

Process : 프로세스를 직접 만들고 관리하는 단위

Queue : 여러 프로세스 간 안전하게 데이터를 주고받는 통신 도구

Pool : 여러 프로세스를 묶어서 효율적으로 작업을 분배하고 실행하는 도구

## 스레드

```md
카페 (프로세스)
├── 직원1 (스레드): 주문 받기
├── 직원2 (스레드): 커피 만들기  
└── 직원3 (스레드): 청소하기
```

### 실제 예시

```python
import threading
import time

def 주문받기():
    print("주문 받는 중...")
    time.sleep(2)
    print("주문 완료")

def 커피만들기():
    print("커피 만드는 중...")
    time.sleep(3)
    print("커피 완성")

# 한 명이 순서대로 (총 5초)
주문받기()
커피만들기()

# 두 명이 동시에 (총 3초)
t1 = threading.Thread(target=주문받기)
t2 = threading.Thread(target=커피만들기)

t1.start()  # 직원1 일시작
t2.start()  # 직원2 일시작
```

## 요약

- I/O-bound: threading
- CPU-bound: cpu를 이용해서 계산 빨리

## FastAPI + BackgroundTasks

### PyTorch

```python
# 설치 없이 바로 사용 가능
print("안녕")
len([1, 2, 3])
sum([1, 2, 3])
range(10)
```

multi process ->청크

## from abc import ABC, abstractmethod

## Stra

## type 기본: List,Dict, Optional

```python
def greet(name: Optional[str] = None) -> str:
    if name:
     return f"Hello,{name}"
    return "Hello,~"
```

## Union Any, Literal

```python
def parse(value:Union[str,int])-> str:
return str(value)
```

> [] 제네릭(Generic) 타입 힌트

## Union과 Any, Literal

Union
한국어로 옮기면 보통 합집합 또는 or타입이라고 설명한다.

Literal

```python
from typing import Literal

def direction(move: Literal["UP", "DOWN", "LEFT", "RIGHT"]):
    print(f"이동: {move}")

```

## Generic

## Protocol- Duck Typing 위한 정적 검사

## Callable - 함수 타입 정의

함수를 인자로 받는 함수의 타입을 명확하게 정의하는 예제

```python
from typing import Callable
def compute(x: int, y: int, op: Callable[[int, int],
int]) -> int:
return op(x, y)
result = compute(3, 4, lambda a, b: a + b)
```

# 💡 궁금한 점

- FastAPI랑 RestAPI차이가 뭔가요?

- 왜 두개를 같이 쓰는거야? 프레임워크 fast api 만써도되는거아님?
