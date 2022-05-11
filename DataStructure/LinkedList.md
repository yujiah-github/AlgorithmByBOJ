## 연결 리스트란?
- 연결 리스트란 **노드를 연결시킨 자료구조**
- 노드는 **연결 리스트에서 데이터를 갖고 있는 데이터의 묶음**
- 노드 속에 **다음 노드를 가리킴**
- 제일 앞에 있는 노드는 **헤드(head)**, 제일 끝 노드는 **테일(tail)**

![](https://velog.velcdn.com/images/cil05265/post/9666ad96-9ee2-4cc8-af07-01ce8630f955/image.png)

### 연결 리스트를 사용하는 이유
- 연결 리스트의 가장 큰 장점은 리스트의 길이가 **가변적**이라는 것이다. 배열은 **가변적이지 않기 때문에** 단점을 연결 리스트가 커버 할 수 있다.
- 연결 리스트는 **다음 노드만 추가하면 되기 때문에** 리스트의 사이즈를 조정하는데에 그리 큰 비용을 들이지 않는다.
- 그러나 연결 리스트는 어떤 노드를 탐색하거나 데이터를 변경할때 바로 찾아낼 수가 없다.
- 그러니까 **데이터가 자주 추가되거나 가변적으로 자주 변하게 될 프로그램이라면 연결 리스트를 쓰는 것이 좋고**, 주로 **데이터의 변경이나 탐색을 위한 것이라면 배열을 쓰는 것이 좋다.**


**저는 p.112부터 p.127까지 발표를 맡았는데, 주로 코드 설명이 대부분인 페이지입니다. 몇 가지 코드만 설명하고 빠르게 진행하갰습니다.**

### 연결 리스트의 구현
#### 연결 리스트에 원소 x 삽입하기(더미 헤드를 두는 버전)
```python
    def insert(self, i:int, newItem):
        if i>= 0 and i <=self.__numItems: #ㅑ=0인 경우, i-1번 노드는 더미 헤드 노드가 됨. i=__numItmes이면 i-1번 노드는 마지막 노드가 됨.
            prev = self.__getNode(i-1) #삽입할 노드의 직전 노드의 레퍼런스인 prev를 찾은 후 x삽입
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems +=1
        else:
            print("index",i, ":out of bound in insert()")
```

#### 연결 리스트에 원소 x 삭제하기(더미 헤드를 두는 버전)

```python
    def remove(self, x): #원소를 주고 원소를 가진 노드 삭제
        (prev, curr) == self.__findNode(x)
        if curr != None:
            prev.next - curr.next
            self.__numItmes -= 1

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return(prev.curr)
            else:
                prev = curr; curr = curr.next

        return(None, none)
```

#### 연결 리스트에 i번 원소 알려주기

```python
    def get(self, i:int):
        if self.isEmpty():
            return None
        if(i>=0 and i<=self.__numItems - 1):
            return self.__getNode(i).item # __getNode(i)를 통해 i번 노드를 찾은 후 해당 노드의 item을 리턴
        else:
            return None
```

#### 연결 리스트에 원소 x 삭제하기(더미 헤드를 두는 버전)

```python
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345
```

#### 전체 코드 확인하기(p.122 - p.126)
![](https://velog.velcdn.com/images/cil05265/post/d20d6a65-7dcc-4f48-9847-8101bf6cfee8/image.jpeg)

![](https://velog.velcdn.com/images/cil05265/post/dfa5a248-c86d-4a30-b940-310239479113/image.jpeg)

![](https://velog.velcdn.com/images/cil05265/post/c533a430-8520-4757-86c7-a7db266aef34/image.jpeg)
