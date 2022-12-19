## Python 기본, 중급 문법 정리
- 알고리즘 문제 풀이 시, 더 효율적으로 문제를 풀기 위함

###  Python Comprehension
- Python의 Comprehension은 한 명령문이 다른 명령문으로부터 변형되어 구축될 수 있게한 기능이다. 
- 종류는 크게 **List Comprehension, Dictionary Comprehension, Set Comprehension**이 있다.

### 1. List Comprehension
- List Comprehension는 입력문으로부터 지정된 표현식에 따라 새로운 리스트 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 갖는다.

> [출력표현식 for 요소 in 입력Sequence [if 조건식]]

```python
oldlist = [1, 2, 'A', False, 3]
newlist = [i*i for i in oldlist if type(i)==int] #oidlist에 있는 요소들 중, int 타입인 요소만 2의 제곱으로 출력
print(newlist)
# 출력: [1, 4, 9]
```

- 여기서 입력 Sequence는 입력으로 사용되는 Iteration이 가능한 데이타 Sequence 혹은 컬렉션이다. 
- 입력 Sequence는 for 루프를 돌며 각각의 요소를 하나씩 가져오게 되고, if 조건식이 있으면 해당 요소가 조건에 맞는지 체크하게 된다. 
- 만약 조건에 맞으면 출력 표현식(Output Expression)에 각 요소를 대입하여 출력 결과를 얻게 된다. 
- 이러한 과정을 모든 요소에 대해 실행하여 결과를 리스트로 리턴하게 된다. 쉽게 설명하면 for 루프를 돌면 특정 조건에 있는 입력데이타를 변형하여 리스트로 출력하는 코드를 간단한 문법으로 표현한 것이다.

### 2. Set Comprehension
- Set Comprehension은 입력 Sequence로부터 지정된 표현식에 따라 새로운 Set 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 갖는다. **List Comprehension과 거의 비슷하지만, 결과가 Set {...}으로 리턴된다는 점이 다르다.**

> {출력표현식 for 요소 in 입력Sequence [if 조건식]}

```python
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist}
print(newlist)
# 출력 : {16, 1, 9, 4}

```

##### 결과 Set은 중복을 허용하지 않으므로 중복된 데이타는 자연스럽게 제거된다. 또한 Set은 요소의 순서를 보장하지 않으므로, 아래 결과에서 보듯이 순서가 랜덤하게 바뀐 결과를 출력하게 된다.

### 3. Dictionary Comprehension
- Dictionary Comprehension은 입력 Sequence로부터 지정된 표현식에 따라 새로운 Dictionary 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 갖는다. Set Comprehension과 거의 비슷하지만, **출력표현식이 Key:Value Pair로 표현된다는 점이 다르며, 결과로 dict 가 리턴된다.**

> {Key:Value for 요소 in 입력Sequence [if 조건식]}

```python
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)
# 출력 : {'박진수': 1, '강만진': 2, '홍수정': 3}
```

```python
def isodd(val):
    return val % 2 == 1

mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)
```