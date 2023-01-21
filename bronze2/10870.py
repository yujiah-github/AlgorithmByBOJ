import sys
n = int(sys.stdin.readline())

lst = [0,1]
for i in range(n-1):
    nextValue = lst[i] + lst[i+1]
    lst.append(nextValue)
    
print(lst[n])