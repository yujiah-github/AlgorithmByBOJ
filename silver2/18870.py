import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().rstrip().split()))
numSet = set(x) #set 함수를 사용하고 다시 list()를 해주어야한다
numSort = list(numSet)
numSort.sort()

numDict = {}
for i in range(len(numSort)):
    numDict[numSort[i]] = i

for i in x:
    print(numDict[i] , end=' ')