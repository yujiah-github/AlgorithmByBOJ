import sys

while True:
    numList = list(map(int, sys.stdin.readline().split()))
    if sum(numList) == 0:
        break
    maxNum = max(numList)
    numList.remove(maxNum)
    if numList[0] ** 2 + numList[1] ** 2 == maxNum ** 2:
        print("right")
    else:
        print("wrong")