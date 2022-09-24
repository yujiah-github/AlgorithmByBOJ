import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, 0, -1):
    if array[i - 1] < array[i]: 
        for j in range(N - 1, 0, -1):
            if array[i - 1] < array[j]:
                array[i - 1], array[j] = array[j], array[i - 1]
                array = array[:i] + sorted(array[i:])
                print(*array)
                exit() 

print(-1) 