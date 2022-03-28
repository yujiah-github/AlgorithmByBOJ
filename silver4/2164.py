import sys
from collections import deque
q = deque()
N = int(sys.stdin.readline())
for i in range(1,N+1):
    q.append(i)
while True:
    q.popleft()
    if len(q)>1:
        x = q[0]
        q.append(x)
        q.popleft()
    else:
        print(q[0])
        