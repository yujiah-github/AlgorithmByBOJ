# 수학
---
## 목차
1. [순열](#1-순열permutation---완전-탐색에서-많이-사용)
2. [조합](#2-조합combination---완전-탐색에서-많이-사용)
3. [math 메서드 정리](#3-math-메서드-정리)
---


### 1. 순열(permutation) - 완전 탐색에서 많이 사용
- 모든 경우의 수를 순서대로 살펴볼 때 용이하다.
- 순서를 정해서 나열하는 것


```python
from itertools import permutations
v = [0,1,2,3]

for i in permutations(v, 4): #뽑을 수의 집합, 몇 개 뽑을 건지. 총 2개의 인수를 전달한다.
    print(i)
```

### 2. 조합(combination) - 완전 탐색에서 많이 사용

- 파이썬에서는 조합까지 기본으로 제공한다.
- 순서를 생각하지 않는 것

```python
from itertools import combinations
v = [0,1,2,3]

for i in combinations(v, 2): #뽑을 수의 집합, 몇 개 뽑을 건지. 총 2개의 인수를 전달한다.
    print(i)
```

### 3. math 메서드 정리

- import math 사용

```python
math.pi 원주율
math.e 자연상수
abs() 절대값 계산 내장 함수
round() 반올림 계산 내장 함수
math.trunc() 버림 계산 함수
math.factorial() 팩토리얼 계산 함수
math.degrees() 라디안을 입력받아 도를 계산
math.radians() 도를 입력받아 라디안을 계산
math.cos() 입력된 라디안에 대한 코사인 값을 계산
math.sin() 입력된 라디안에 대한 사인 값을 계산
math.tan() 입력된 라디안에 대한 탄젠트 값을 계산
math.acos() cos()의 역함수
math.asin() sin()의 역함수
math.atan() tan()의 역함수
math.pow() 제곱 연산
math.sqrt() 제곱근 연산
math.log() 첫 번째 매개변수의 로그를 구합니다.
math.log10() 밑수가 10인 로그를 계산합니다.
math.comb(a,b) 자연수 N과 정수 K가 주어졌을 때 이항계수 구하는 공식
```

- 예시
```python
import math
a, b = map(int,input().split())
print(math.comb(a,b))
```

