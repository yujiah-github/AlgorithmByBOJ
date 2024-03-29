### 1. 배열
> 삽입/삭제: O(N)
탐색: O(1)
- 파이썬에서는 단순히 List로 구현한다.
- **탐색할 때 사용하기 좋은 자료구조(삽입이나 삭제는 한자리씩 뒤로 옮기거나 하는 식으로 이루어질 수 있기 때문에, 시간복잡도가 O(N)이된다.)**

### 2. 벡터 (= 동적배열)
> 삽입/삭제: O(N)
탐색: O(1)
- 파이썬에서는 단순히 List로 구현한다.
- 같은 언어에서는 배열과 벡터는 다르다.
- 하지만 파이썬에서는 배열과 같은 List로 쓰면 된다.
- List 자체가 이미 동적 배열을 지원해주기 때문이다.

### 3. 연결리스트(링크드 리스트)
> 삽입/삭제: O(1)
탐색: O(N)
- 시간복잡도 측면에서 **배열(List)와 반대** 된다. **(탐색을 하려면 순간적으로 포인터 부분을 찍고 찍고 가야 하기 때문에 탐색이 O(N)이 되고, 연결 자체의 앞뒤로 수정만 하면 되므로 삽입/삭제시 시간 복잡도가 O(1)이 된다.**
- 링크드 리스트는 백준 문제를 풀며 막 사용할일이 많지는 않지만, 다른 자료구조 구현에도 많이 쓰이니 이론상 알아둘 필요가 있다.

### 4. 스택 LIFO
> 삽입/삭제: O(1)
- Last In First Out
- 파이썬에서 구현은 List로 한다.

```python
s = [1,2,3,4,5,6]

while(len(s)>0):
 print(s[-1])
    s.pop(-1)
```

- 위의 코드 처럼 구현 되면 되는데,  배열의 마지막 거를 꺼내는 거다.

### 5. 큐 LILO
> 삽입/삭제: O(1)
- 줄서기 Last in Last Out
- **from collections import deque** 로 임포트하여 데큐를 사용한다.

```python
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

while(len(q) >0):
 print(q.popleft())
 ```

- 위 코드에서 보면 **popleft()** 라는 함수를 통해 처음에 있는 값을 빼는데, 덱은 **popright()**라는 함수도 지원한다.
- 또한 파이썬에는 Queue도 있고 Deque도 있는데 Queue는 멀티 스레딩도 지원하는 라이브러리여서 Deque보다 느리다. 알고리즘 문제를 푸는 입장이므로 Deque를 사용하는 것이 더 편하다.

### 6.우선순위큐(내부가 Heap으로 구성)
> 삽입/삭제 : O(logN)

```python
import heapq
```

- 리스트를 하나 만들고 사용한다

```python
pq = []
heapq.heappush(pq,3)
heapq.heappush(pq,1)
heapq.heappush(pq,2)

while(len(pq) >0):
 print(heapq.heappop(pq))
 ```

- 파이썬은 MinHeap 이다.**(이진트리의 최상위는 항상 최소값이다)**
- 우선 순위 큐 같은 경우에는 , 문제를 풀면서 여러 값들을 넣고 뺄때마다 젤 작은 값이나 젤 큰 값을 알아야 할 때 써야 한다. **Sort() 같은 경우 전체 리스트 자체를 정렬해준다는 점에서 큰 차이점을 가진다.**

### 7. Map(딕셔너리)
> 삽입/삭제: O(1)
- 파이썬은 딕셔너리를 사용하면 된다.
- 추가로, c++같은 경우는 **O(logN)**이 되는데 이는 c++의 맵은 속을 들여다 보면 이진 그래프로 구현이 되어있기 때문이고, python의 딕셔너리의 경우는 해시로 구현이 되어있기 때문이다.

### 8. 집합(set)
> 삽입/삭제: O(logN)
- 중복을 제거하는게 큰 특징!
