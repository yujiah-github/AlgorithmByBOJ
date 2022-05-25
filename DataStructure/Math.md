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