import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    distance = y - x
    cnt = 0
    moving = 1 
    moving_cnt = 0
    while moving_cnt < distance :
        cnt += 1
        moving_cnt += moving
        if cnt % 2 == 0 :
            moving += 1  
    print(cnt)