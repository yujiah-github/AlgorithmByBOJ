import sys
n = int(sys.stdin.readline()) #수를 입력 받음
numbers = map(int, sys.stdin.readline().strip().split())
    
cnt = 0 #소수의 개수를 세는 카운터

for num in numbers:
    error = 0
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                error += 1
        if error == 0:
            cnt += 1

print(cnt)