## 수학
### 공식
- import math 사용
#### 1. 이항 계수 공식
- **자연수 N과 정수 K**가 주어졌을 때 이항계수 구하는 공식
```python
math.comb()
```
```python
import math
a, b = map(int,input().split())
print(math.comb(a,b))
```

#### 2. 순열(permutation) - 완전 탐색에서 많이 사용
- 모든 경우의 수를 순서대로 살펴볼 때 용이하다.
- 순서를 정해서 나열하는 것


```python
from itertools import permutations
v = [0,1,2,3]

for i in permutations(v, 4): #뽑을 수의 집합, 몇 개 뽑을 건지. 총 2개의 인수를 전달한다.
    print(i)
```

#### 3. 조합(combination) - 완전 탐색에서 많이 사용

- 파이썬에서는 조합까지 기본으로 제공한다.
- 순서를 생각하지 않는 것

```python
from itertools import combinations
v = [0,1,2,3]

for i in combinations(v, 2): #뽑을 수의 집합, 몇 개 뽑을 건지. 총 2개의 인수를 전달한다.
    print(i)
```
