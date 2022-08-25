import sys
T = int(sys.stdin.readline())

for i in range(T) :
    N = int(sys.stdin.readline())
    lst = [0]*N
    for j in range(N) :
            T1 ,T2 = map(int,sys.stdin.readline().split())
            lst[j] = [T1,T2]

    people_lst = sorted(lst, key = lambda x : x[0])
    hired = 1
    man = people_lst[0][1]
    for j in range(1,N) :
        if people_lst[j][1] < man :
            man = people_lst[j][1]
            hired += 1

    print(hired)