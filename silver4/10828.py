import sys

N = int(sys.stdin.readline())
list = []
for i in range(N):
    T = sys.stdin.readline().split()
    if T[0] == "push":
        list.append(T[1])
    
    elif T[0] == "pop":
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop())
            
    elif T[0] == "size":
        print(len(list))
    
    elif T[0] == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)
            
    elif T[0] == "top":
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])