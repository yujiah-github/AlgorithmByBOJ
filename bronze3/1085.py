#그림으로 나타내면 아래와 같다.
#직사각형의 경계까지 더 빨리가는 방법을 구하는 것이므로, x좌표, y좌표, w-x좌표, h-y좌표 거리 중 최솟값을 구하면 된다.
#w,h가 x와 y보다 크므로, w,h가 작은 경우는 생각하지 않아도 된다.
import sys
x, y, w, h = map(int, sys.stdin.readline().strip().split())
numList = []
numList.append(x)
numList.append(y)
numList.append(w-x)
numList.append(h-y)
print(min(numList))