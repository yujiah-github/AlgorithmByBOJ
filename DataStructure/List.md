## 리스트를 이용한 스택
### 1. 리스트 스택의 객체 구조
- 파이썬에서 리스트는 배열로 구현되어 있으므로 리스트를 이용한 스택은 사실상 **배열을 이용한 스택**이라 할 수 있다.

### 2. 리스트 스택의 작업과 구현
- 파이썬 리스트를 이용해서 스택 **ListStack**을 구현한다.
```python
class ListStack:
    def __init__(self): #모든 클래스에 공통적인 이름으로 해당 클래스의 객체가 생성될 때 수행되는 메서드. 생성자라고도 하며, 빈 리스트 __stack[]을 생성.
        self.__stack = [] #스택에 원소들이 저장되는 리스트
    
    def push(self, x): #스택의 맨 위에 있는 원소 x를 삽입
    
    def pop(self): #스택의 맨 위에 있는 원소를 알려주고 삭제한다.

    def top(self): #스택의 맨 위에 있는 원소들을 알려준다.

    def isEmpty(self): #스택이 비었는지 알려준다.

    def popAll(self): #스택을 깨끗이 청소한다.

```

#### 원소 삽입
- 스택에 새 원소를 삽입할 때는 스택 탑 바로 윗자리에 원소를 저장한다.
- 리스트에서는 **맨 끝 원소 다음**에 원소를 삽입하면 된다.
- 리스트의 맨 끝에 원소를 추가하는 메서드는 **append()** 이다.

```python
#코드 예시
def push(self, x):
    self.__stack.append(x)
```

#### 원소 삭제
- 스택에 있는 원소를 삭제할 때는 무조건 탑에 있는 원소를 삭제한다.
- 리스트에서 삭제를 하는 메서드는 **pop()** 이다.

```python
#코드 예시
def pop(self):
    return self.__stack.pop()
```
>그림 예시(직접 그림)
![](https://velog.velcdn.com/images/cil05265/post/6164ec81-d316-40ea-8365-4103680a9ab5/image.jpg)


#### 스택의 탑 원소 반환
- 리스트의 마지막 원소 리턴
```python
#코드 예시
def top(self):
    if self.isEmpty(): 
        return None #스택이 비어있으면 반환할 원소가 없음
    else:
        return self.__stack[-1] #리스트의 맨 끝 원소를 반환
```

#### 스택이 비었는지 확인
- **bool() 메서드** 를 이용한다.

```python
#코드 예시
def isEmpty(self) -> bool:
    return not bool(self.__stack)
    # return len(self.__stack)==0
```

#### 스택 비우기

- 스택을 완전히 비워버린다.

```python
#코드 예시
def popAll(self):
    self.__stack = []
    # self.__stack.clear()
```

### 전체 코드
![](https://velog.velcdn.com/images/cil05265/post/dccd22a1-db4b-4652-8fa3-fe246ed83bce/image.jpeg)

### 백준에서 풀어보면 좋은 스택 활용 문제들(직접 풀어본 문제들입니다)
#### 10828번 스택
![](https://velog.velcdn.com/images/cil05265/post/29e2c7cb-881e-479d-a562-338e869eb390/image.png)

```python
import sys
n = int(sys.stdin.readline()) #명령의 수 입력
stack = [] #리스트 생성
for i in range(n):
    x = sys.stdin.readline().split() #명령어와 숫자 입력
    
    if x[0] == 'push': #명령어가 푸쉬인 경우
        stack.append(x[1]) #list_num에 추가 (입력값이 명령어와 숫자로 구성되어 있으므로 인덱스는 0과 1밖에 없다)
    
    elif x[0] == 'pop': #명령어가 팝인 경우
        if len(stack) == 0:
            print(-1) #정수가 없으면 -1을 출력
        else:
            print(stack.pop()) #제거
            
    elif x[0] == 'size': #명령어가 size인 경우
        print(len(stack))
    
    elif x[0] == 'empty': #empty인 경우
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif x[0] == 'top':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])
```
#### 10733번 제로
![](https://velog.velcdn.com/images/cil05265/post/0b09fcdb-6632-4194-b5a9-41cd07c899f0/image.png)
```python
import sys
n = int(sys.stdin.readline())
stack = []
sum = 0
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        sum = sum - stack[len(stack)-1]
        stack.pop()
    else:
        stack.append(x)
        sum += x
print(sum)
```

#### 9012번 괄호
![](https://velog.velcdn.com/images/cil05265/post/595fd2b0-9616-437f-b94d-5a6de98cc850/image.png)

```python
import sys
t = int(sys.stdin.readline())
for i in range(0, t):
    st = 0
    string = sys.stdin.readline()
    for c in string:
        if c == '(':
            st += 1
        elif c == ')':
            if st == 0:
                print('NO')
                break
            else:
                st -= 1
        else:
            if st == 0:
                print('YES')
            else:
                print('NO')
```

#### 4949번 균형잡힌 세상
![](https://velog.velcdn.com/images/cil05265/post/b64fa9d1-8deb-4127-a9e6-a591028b0028/image.png)
```python
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
```

#### 1874번 스택 수열
![](https://velog.velcdn.com/images/cil05265/post/8a457f04-2d50-419a-9259-d2f0d98a2f30/image.png)

```python
n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               

if flag == 0:
    for i in answer:
        print(i)
```
#### 여담
- 제가 어울림 마지막 날까지, 백준 알고리즘 티어 골드를 찍는지 못찍는지 내기를 하기로 했습니다!!! 현재 실버 1입니다ㅋㅋ 여러분도 내기 같이 하실래여?
![](https://velog.velcdn.com/images/cil05265/post/723b4894-570a-4676-a2ef-4e6ebcd2bf0a/image.png)
