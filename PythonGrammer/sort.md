## 정렬
> sorted()
1. 원본 내용을 바꾸지 않고, 정렬한 값을 반환한다.
2. List, tuple, Dictionary, str에 모두 사용 가능하다.
3. key 를 통하여 정렬할 기준을 정할 수 있다.
4. **reverse 가 True이면 내림차순, False이면 오름차순으로 정렬된다**

> sort()
1. 원본 자체를 수정한다.
2. 반환값은 None
3. **Tuple , Dictionary, Str 에는 사용이 불가하다.**

>array.sort(key = lambda x:x[0])
1. sort 함수를 사용한 람다식 조건(x[0]의 오름차순으로 정렬)

>sorted(array, key = lambda x: x[0]))
1. sorted 함수를 사용한 람다식 조건(x[0]의 오름차순으로 정렬)

>array.sort(key=lambda x: len(x))
1. sort 함수를 사용하여 길이 순으로 정렬

>array.sort(key = lambda x: (x[1], -x[2]))
1. sort 함수를 사용하여 x[1]의 오름차순, -x[2]의 내림차순으로 정렬

