import sys,math
n = int(sys.stdin.readline())
for i in range(n):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    distance = math.sqrt((lst[0] - lst[3])**2 + (lst[1]-lst[4])**2)
    if distance == 0 and lst[2] == lst[5]:
        print(-1)
    elif distance == lst[2] + lst[5] or distance == abs(lst[2] - lst[5]):
        print(1)
    elif abs(lst[2] - lst[5]) < distance < lst[2]+lst[5]:
        print(2)
    else:
        print(0)