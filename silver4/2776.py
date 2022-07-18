import sys
T = int(input())
for _ in range(T):
    N = int(input())
    num1 = set(sys.stdin.readline().split())
    M = int(input())
    num2 = list(sys.stdin.readline().split())
    for i in num2:
        if i in num1:
            print(1)
        else:
            print(0)