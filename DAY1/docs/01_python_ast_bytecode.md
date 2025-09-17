# 📌 Python 실행 구조 정리

## 1. 실행 과정

1. **소스 코드 작성**
   ```python
   a = 1 + 2
   Lexing / Tokenizing
   ```

코드 문자열을 토큰 단위로 쪼갬

예: ['a', '=', '1', '+', '2']

Parsing

토큰을 문법 규칙에 맞게 분석하여 트리 구조(AST) 생성

바이트코드 변환

AST → 바이트코드(.pyc 파일로 저장)

실행

Python Virtual Machine(PVM)이 바이트코드를 실행

2. Python Virtual Machine (PVM)
   파이썬은 인터프리터 언어

.py 파일을 한 줄씩 읽어 실행

하지만 단순히 “줄 단위 실행”이 아니라, 중간 단계인 바이트코드(Bytecode) 를 거침

바이트코드는 플랫폼 독립적이며, 실행 속도를 높이기 위해 .pyc 파일로 캐싱됨

3. AST (Abstract Syntax Tree)
   소스코드를 트리 구조로 표현한 것

예시:

python
코드 복사
a = 1 + 2
AST 구조:

scss
코드 복사
Assign
├─ Name(a)
└─ BinOp
├─ Constant(1)
├─ Add()
└─ Constant(2) 4. 파이썬 바이트코드
소스코드 파싱 후 생성되는 중간 표현 (Intermediate Representation)

.pyc 파일에 저장되며, PVM이 이를 실행

특징:

실행 속도 향상 (한 번 생성 후 재사용 가능)

OS와 독립적인 추상 명령어 수준
