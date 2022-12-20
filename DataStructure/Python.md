# Python 기본, 중급 문법 정리
- 알고리즘 문제 풀이 시, 더 효율적으로 문제를 풀기 위함

---
## 목차
1. [Python Comprehension](#1-list-comprehension)
2. [sort()와 sorted()의 차이](#sort와-sorted의-차이)
3. [Python 자료형 정리](#python-자료형-정리)
---

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

### sort()와 sorted()의 차이
#### sort()
- 리스트 메서드에서 정렬을 하는 것이다.
- 원래의 목록에 영향이 있다.

```python
a = [1,3,2,5,4]
a.sort()
print(a)
# [1,2,3,4,5]
```
##### 내림차순으로 정렬할 때는 해당 방법을 사용한다.

```python
a = [1,3,2,5,4]
a.sort(reverse = True)
print(a)
# [5,4,3,2,1]
```

#### sorted()
- 파이썬 표준 내장함수로써 정렬을 하는 것이다.
- 새로운 정렬 결과를 반환한다. 원래 목록에 영향을 끼치지 않는다.

##### 내림차순으로 정렬할 때는 해당 방법을 사용한다

```python
b = [1,3,2,5,4]
result = sorted(b, reverse = True)
print(result)
print(b)
# [5,4,3,2,1]
```

### Python 자료형 정리
|분류 | 타입 | 특징 | 예시 |
|----|----|----|----|
|시퀀스(sequence) |리스트(list)| 순서가 있고, 가변(mutable) |[1, 2, 3]
|시퀀스(sequence) |튜플(tuple) |순서가 있고, 불변(immutable) |(1, 2, 3)
|세트(set)| 세트(set)| 순서가 없고, 중복을 허용하지 않음 |{1, 2, 3} |
|맵(map) | 딕셔너리(dictionary)| 순서가 없고, key/value 쌍으로 이루어짐| {'a': 1, 'b': 2, 'c': 3}|

#### 리스트(List)
- 순서가 있고 변할 수 있다.
- 따라서 다양한 종류의 내장 메서드를 가지고 있다.

```python
len(list) : 리스트의 전체 길이
max(list) : 리스트 안에 있는 요소 중에서 최대값 반환 (문자인 경우 알파벳 순서 기준)
min(list) : 리스트 안에 있는 요소 중에서 최소값 반환 (문자인 경우 알파벳 순서 기준)
list(seq) : 튜플을 리스트 자료형으로 변환
list.append(obj) : 기존 리스트에 1개의 요소를 이어 붙이기
list.extend(seq) : 기존 리스트에 다른 리스트를 이어 붙이기
list.count(obj) : 리스트 안에 obj 가 몇 개 들어있는지 세어서 개수를 반환
list.index(obj) : 리스트에서 obj 요소 값이 있는 가장 작은 index 값 반환
list.insert(index, obj) : 기존 리스트의 index 위치에 obj 값을 삽입
list.pop(obj=list[-1]) : 기존 리스트에서 마지막 요소를 제거하고, 제거된 마지막 요소를 반환
list.remove(obj) : 기존 리스트에서 remove(obj) 메소드 안의 obj 객체를 제거
list.reverse() : 리스트의 객체를 리스트 안에서 순서를 반대로 뒤집기
list.sort() : 리스트의 객체를 리스트 안에서 순서대로 정렬하기 (디폴트 오름차순)
```


#### 튜플(Tuple)
- 리스트와 달리 순서가 있고 변하지 않는다.
- 따라서 리스트보다 내장 함수의 수가 현저히 적은 편이다.
- 슬라이싱 하는 방법은 리스트와 동일함.

```python
len(tuple) #튜플의 길이
max(tuple) #튜플의 최댓값
min(tuple) #튜플의 최솟값
tuple(seq) #시퀀스를 튜플화
tuple.count() #튜플의 개수세기
tuple.index() #튜플의 인덱스 반환
```

#### 세트(Set)

#### 딕셔너리(Dictionary)

```python
len(dict): 사전의 총 길이 (total length of Dictionary)
str(dict): 사전을 문자열로 반환 (string representation of a Dictionary)
type(variable): 입력 변수의 유형 반환 (returns the type of the passed variable)
dict.keys(): 사전의 키 목록
dict.values(): 사전의 값 목록
dict.items(): 사전의 (키, 값) 튜플 목록
dict.clear(): 사전의 모든 {키, 값} 셋 제거
dict.copy(): 사전의 {키 : 값} 셋 복사
dict.fromkeys(seq, value): seq, value 셋으로 신규 사전 생성
dict.get(key, default=None): 키에 할당된 값 반환
dict.setdefault(key, default=None) : 키에 할당된 값 반환
dict.update(dict2): 기존 사전에 새로운 사전 dict2 추가
```