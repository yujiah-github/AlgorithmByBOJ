## 힙 작업 알고리즘과 구현
- 힙을 잘 다루려면 트리에 대한 지식도 있어야합니다.
- **트리 -> 힙 -> 코드** 순서대로 발표 진행하겠습니다.

### 1. 트리란?
- 자료구조에서 트리는 **부모 - 자식 관계**로 정의하고, 부모에서 자식으로 간선이 이어져 있는 **유향 그래프***이다.
- 자료구조에서 트리는 **부모가 없는 루트 노드를 정의**한다.

![](https://velog.velcdn.com/images/cil05265/post/a5db801e-8f1a-4b77-b052-b82d6bfd80f1/image.png)
![](https://velog.velcdn.com/images/cil05265/post/cb93e901-e3da-403a-bfaf-40856cfa7755/image.png)


- 트리는 항상 **루트(Root)** 에서부터 시작된다. 
- 루트는 **자식(Child) 노드**를 가지며, **간선(Edge)** 으로 연결되어 있다.

> **노드** : 트리를 구성하는 기본 원소<br>
**루트 노드** : 트리에서 부모가 없는 최상위 노드, 트리의 시작점 <br>
**부모 노드** : 루트 노드 방향으로 직접 연결된 노드<br>
**자식 노드** : 루트 노드 반대 방향으로 직접 연결된 노드<br>
**형제 노드** : 같은 부모 노드를 갖는 노드들<br>
**리프 노드**: 루트 노드를 제외한 차수가 1인 정점을 뜻한다. 즉, 자식이 없는 노드라는 것이다. **단말 노드** 라고 부르기도 한다.

- 자식 노드의 개수는 **차수(Degree)** 라고 하며, 크기(Size)는 **자신을 포함한 모든 자식 노드의 개수**다.
- 높이(Height)는 **가장 긴 루트 경로의 길이** 까지의 거리, 깊이(Depth)는 **루트에서부터 현재 노드** 까지의 거리다.
- 트리는 그 자식도 트리인 **서브트리(Subtree)** 구성을 띤다.
- 레벨(Level)은 **0** 에서부터 시작하고 노드까지 연결된 **간선 수의 합**을 의미한다.
- 트리는 항상 **단방향(Uni-Directional)** 이기 때문에, 간선의 화살표는 생략 가능하다. 그림에서도 마찬가지로 생략해서 표현했고 일반적으로 방향은 **위에서 아래** 로 향한다.

### 2. 이진 트리

![](https://velog.velcdn.com/images/cil05265/post/e785d6b8-0179-40f0-8650-9f7f87211084/image.png)


- 부모 노드 밑의 **자식 노드 개수(=차수, degree)를 최대 2개로 제한** 하는, 트리의 가장 간단한 형태다. 두 자식 노드를 보통 왼쪽 자식과 오른쪽 자식으로 구분짓는다.

##### 이진트리의 종류는 다음과 같다.

![](https://velog.velcdn.com/images/cil05265/post/588e3708-c114-4e2b-8968-5d6c72dc54e3/image.png)

1. **정 이진 트리(full binary tree)**: 모든 트리의 자식은 0개나 2개다.

2. **포화 이진 트리(perfect binary tree)**: 모든 리프 노드의 높이가 같고 **리프 노드가 아닌 노드는 모두 2개의 자식을 갖는다.** 이진 트리에서 리프 높이의 최대치가 n일 때 가장 많이 존재할 수 있는 노드의 수는 2n-1개인데 포화 이진 트리는 이 개수를 모두 채운 이진 트리라고도 볼 수 있다. 또한, 모든 포화 이진 트리는 정 이진 트리이다.

3. **완전 이진 트리(complete binary tree)**: 모든 리프노드의 높이가 최대 1 차이가 나고, 모든 노드의 오른쪽 자식이 있으면 왼쪽 자식이 있는 이진트리이다. **다시 말해 트리의 원소를 왼쪽에서 오른쪽으로 하나씩 빠짐없이 채워나간 형태이다.** 포화 이진 트리는 완전 이진 트리의 부분집합이다. 단, 포화 이진 트리가 아닌 완전 이진 트리는 정 이진 트리일 수도 있고 아닐 수도 있다.

##### 완전 이진 트리의 경우 왼쪽부터 빠짐없이 채워져있다는 성질을 이용해 배열을 사용하여 구현 하기도 한다. 1번부터 시작하는 배열을 생각하면 n번째 원소의 왼쪽 자식은 2n, 오른쪽 자식은 2n+1번째 원소로 구성하면 된다. 또 n번째 원소의 부모 노드는 [n/2]번째 원소가 된다.

#### 2.1 이진 트리 순회 방법
- **중위 순회(In-order traversal)** : 왼쪽 자손, 자신, 오른쪽 자손 순서로 방문하는 순회 방법. 이진 탐색 트리를 중위 순회하면 정렬된 결과를 얻을 수 있다. 스택을 통해 구현 가능.
- **전위 순회(Pre-order traversal)**: 자신, 왼쪽 자손, 오른쪽 자손 순서로 방문하는 순회 방법. 스택을 통해 구현 가능.
- **후위 순회(Post-order traversal** : 왼쪽 자손, 오른쪽 자손, 자신 순서로 방문하는 순회 방법. 스택을 통해 구현 가능.
- **레벨 순서 순회(Level-order traversal)**: 너비 우선 순회(Breadth-First traversal)라고도 한다. **큐를 통해 구현 가능.**

다음의 사진을 보세요.
![](https://velog.velcdn.com/images/cil05265/post/3b43ac31-ff1f-4a2f-813d-1939507ff9df/image.gif)

순회 방법에 따라 경로가 다릅니다.

- **중위 순회(In-order traversal)** : 1 3 4 6 7 8 10 13 14
- **전위 순회(Pre-order traversal)**: 8 3 1 6 4 7 10 14 13
- **후위 순회(Post-order traversal** : 1 4 7 6 3 13 14 10 8
- **레벨 순서 순회(Level-order traversal)**: 8 3 10 1 6 14 4 7 13

### 3. 이진 탐색 트리
![](https://velog.velcdn.com/images/cil05265/post/f4d88b4b-98da-4c5d-8df1-febaaaf08123/image.png)

- 이진 트리의 일종으로, 노드의 왼쪽 가지에는 노드의 값보다 **작은 값** 들만 있고, 오른쪽 가지에는 **큰 값** 들만 있도록 구성되었다. 자식 노드들도 동일한 방법으로 정렬되어 노드의 왼쪽 자식의 왼쪽 가지에는 왼쪽 자식이 가진 값보다 작은 값만 있고, 왼쪽 자식의 오른쪽 가지에는 왼쪽 자식의 값보다 큰 값들만 있다. **이진 탐색 트리의 어느 노드를 잡아도 동일한 규칙으로 정렬이 되어 있다.**

- 이렇게 구성해 두면 어떤 값 n을 찾을 때, **루트 노드와 비교해서 n이 더 작다면 루트 노드보다 큰 값들만 모여 있는 오른쪽 가지는 전혀 탐색할 필요가 없다.** 마찬가지로 루트 노드의 왼쪽 자식보다 n이 크다면 왼쪽 자식의 왼쪽 가지는 탐색할 필요가 없다. **다시 말해 트리 자체가 이진 탐색을 하기에 적합한 구성이 되는 것이다.** 또한 값을 찾을 때뿐만이 아니라 값을 삽입하거나 삭제할 때도 똑같은 과정을 거치므로, 이상적인 상황에서 탐색/삽입/삭제 모두 시간복잡도가 **O(log N)** 이 된다.

![](https://velog.velcdn.com/images/cil05265/post/a8c2e12e-27cc-46f4-b990-e79a445d0b21/image.png)

> 예시) 8 찾기
    1. 루트 노드 15보다 작으므로 **왼쪽** 으로 이동한다. <br>
    2. 노드 10보다 크므로 **오른쪽** 으로 이동한다. <br>
    3. 노드 5보다 크므로 **오른쪽** 으로 이동한다. <br>
    4. 노드 7보다 크므로 **오른쪽** 으로 이동한다. <br>

### 4. 힙 트리
![](https://velog.velcdn.com/images/cil05265/post/6bd52189-79f6-4ed4-939e-d0a925f8fd46/image.png)

- 영단어 힙(heap)은 **'무엇인가를 차곡차곡 쌓아올린 더미'** 라는 뜻을 지니고 있다.
- 힙은 항상 **완전 이진 트리** 의 형태를 띠어야 하고, 부모의 값은 항상 자식(들)의 값보다 크거나 **(Max heap 최대 힙)**, 작아야 **(Min heap 최소 힙)** 하는 규칙이 있다.
- 따라서 루트노드에는 항상 데이터들 중 가장 큰 값(혹은 가장 작은 값)이 저장되어 있기 때문에, 최댓값(혹은 최솟값)을 O(1)안에 찾을 수 있다.
- 완전 이진 트리를 사용하는 이유는 **삽입/삭제의 속도** 때문이다.

### 5. 힙의 데이터 처리
- 데이터의 삽입과 삭제는 모두 **O(logN)** 이 소요된다.

#### 5.1 데이터 삽입
![](https://velog.velcdn.com/images/cil05265/post/98caeeb6-f577-466f-9ee7-ab433d24e859/image.png)

1. 가장 끝의 자리에 노드를 삽입한다.
2. 그 노드와 부모 노드를 서로 비교한다.
3. 규칙에 맞으면 그대로 두고, 그렇지 않으면 부모와 교환한다.
4. 규칙에 맞을 때까지 3번 과정을 반복한다.

#### 5.2 데이터 삭제
![](https://velog.velcdn.com/images/cil05265/post/6c7acfaf-e68a-4b18-b6cd-0d74ccc789fa/image.png)
1. 루트 노드를 제거한다.
2. 루트 자리에 가장 마지막 노드를 삽입한다.
3. 올라간 노드와 그의 자식 노드(들)와 비교한다.
4. 조건에 만족하면 그대로 두고, 그렇지 않으면 자식과 교환한다.
- 최대 힙
    - 부모보다 더 큰 자식이 없으면 교환하지 않고 끝낸다.
    - 부모보다 더 큰 자식이 하나만 있으면 그 자식하고 교환하면 된다.
    - 부모보다 더 큰 자식이 둘 있으면 자식들 중 큰 값과 교환한다.

- 최소 힙
    - 부모보다 더 작은 자식이 없으면 교환하지 않고 끝낸다.
    - 부모보다 더 작은 자식이 하나만 있으면 그 자식하고 교환하면 된다.
    - 부모보다 더 작은 자식이 둘 있으면 자식들 중 작은 값과 교환한다.
5. 조건을 만족할 때까지 4의 과정을 반복한다.

### 6. 힙의 표현
![](https://velog.velcdn.com/images/cil05265/post/dae63870-a8dc-4d7d-860e-cd1517e56e29/image.png)


- 이진 힙은 **완전 이진 트리(Complete Binary Tree)로서** , 배열로 표현하기 매우 좋은 구조다. 트리의 배열 표현의 경우 계산을 편하게 하기 위해 **인덱스는 1부터 사용한다.**
- 해당 노드의 인덱스를 알면 깊이가 얼마인지, 부모와 자식 노드가 배열 어디에 위치하는지 바로 알아낼 수 있다. **깊이는 1, 2, 4, 8, ... 순으로 2배씩 증가** 하며, 인덱스는 1부터 시작했기 때문에 부모/자식 노드의 위치는 각각 **부모 i-1/2** , **왼쪽 자식 2i** , **오른쪽 자식 2i+1** 의 간단한 수식으로 계산할 수 있다.
- 물론 꼭 완전 이진 형태가 아니어도 비어있는 위치는 얼마든지 널(Null)로 표현할 수 있기 때문에, 사실상 모든 트리는 배열로 표현이 가능하다.
- 힙의 형태를 보면 **최대 힙의 경우 루트가 항상 최댓값이고** , **최소 힙의 경우 루트가 항상 최솟값** 임을 알 수 있다.
- 이를 이용하여 **우선순위 큐(priority queue)** 를 구현하거나, **힙 정렬(heap sort)** 을 만드는 등의 일을 할 수 있다.

### 7. 힙 알고리즘 구현
#### 7.1 힙에 원소 삽입하기
```python
def insert(self, x): #x는 삽입할 원소
    i = len(self.__A)
    self.__A[i] = x
    parent = (i-1) //2
    while i>0 and A[i] > A[parent]: #부모의 값과 비교해서 힙의 특성을 깨면 자리를 맞바꿈
        self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
        i = parent
        parent = (i-1) // 2
```

#### 7.2 힙에서 원소 삭제하기

```python
def deleteMax(self):
    if (not self.isEmpty()):
        max = self.__A[0]
        self.__A[0] = self.__A.pop()
        self.percolateDown(8)
        return max
    else:
        return None
```
#### 7.3 전체코드
![](https://velog.velcdn.com/images/cil05265/post/a0bf87b0-1b5d-4e9f-a150-a3d049125c92/image.jpeg)

### 8. 힙 관련 백준 문제
1. 최소 힙
- 문제
![](https://velog.velcdn.com/images/cil05265/post/512b0452-bde0-4489-a86d-5e150c6852eb/image.png)

- 코드
```python
import sys
import heapq

n = int(sys.stdin.readline())
heap = [] # 배열

# 연산의 개수만큼 반복한다.
for i in range(n):
    x = int(sys.stdin.readline())

    # x가 0이라면 배열에서 가장 작은 값을 출력한다.
    if x == 0:

        # 배열이 비어 있으면 0을 출력한다.
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    # x가 0이 아니라면 배열에 x를 힙 푸시한다.
    else:
        heapq.heappush(heap, x)
```

2. 최대 힙

- 문제
![](https://velog.velcdn.com/images/cil05265/post/a4c64d7d-4401-4bea-951a-bf87755c983f/image.png)

- 코드
```python
import sys
import heapq

n= int(sys.stdin.readline())
heap = []
for _ in range(n) :
    x = int(sys.stdin.readline())
    if x :
        heapq.heappush(heap, (-x, x))
    else :
        if len(heap) >= 1 :
            print[heapq.heappop(heap](1))
        else :
            print(0)
```
3. 절댓값 힙
- 문제
![](https://velog.velcdn.com/images/cil05265/post/b1cb4fbe-b3d4-4d24-8ca5-eecbd6e8bead/image.png)


- 코드

```python
import sys
import heapq

numbers = int(sys.stdin.readline())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print[heapq.heappop(heap](1))
        except:
            print(0)
```

### 9. 여담
![](https://velog.velcdn.com/images/cil05265/post/ee96d8f1-9a96-4bea-bcc4-e90a19050702/image.png)
- **골드** 달성했습니다!!