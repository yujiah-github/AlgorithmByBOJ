## 우선순위 큐
- 문제풀이 할 때, heap을 사용
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
