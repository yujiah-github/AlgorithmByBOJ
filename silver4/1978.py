import sys
n = int(sys.stdin.readline()) #수를 입력 받음
list = []

for i in range(n):
    num = int(sys.stdin.readline().strip().split())
    list.append(num)
    
cnt = 0 #소수의 개수를 세는 카운터

for i in range(n):
    x = list[i]
    if x < 2:
        continue #중첩문을 중지하지 않고, 다음 조건으로 넘어가기 위함
    def is_prime_num(x):
        for j in range(2, x):
            if x % j == 0:
                continue #중첩문을 중지하지 않고, 다음 조건으로 넘어가기 위함
        cnt += 1 #소수가 맞으면 카운터를 하나 증가

print(cnt)