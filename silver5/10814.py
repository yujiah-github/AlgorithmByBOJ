import sys

N =  int(sys.stdin.readline())
list = []

for i in range(N):
    age,name = map(str, sys.stdin.readline().split())
    age = int(age)
    list.append((age,name))
    
list.sort(key = lambda x : x[0])

for i in list:
    print(i[0], i[1])