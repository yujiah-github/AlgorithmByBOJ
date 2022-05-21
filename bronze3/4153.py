#세 수를 입력 받고, 리스트로 만들어 준다.
#리스트에서 가장 큰 수를 고른다.
#피타고라스 정리를 활용하여 식을 만들어주고 직각이 맞으면 right, 틀리면 wrong을 반환한다.
# 000이 입력 되면, 프로그램을 종료한다.
import sys
while True:
    numList = list(map(int, sys.stdin.readline().strip().split()))
    if sum(numList) == 0:
        break
    maxNum = max(numList)
    numList.remove(maxNum)
    if numList[0]**2 + numList[1] **2 == maxNum ** 2:
        print("right")
    else:
        print("wrong")