from collections import deque
import sys

dq = deque()
N = int(sys.stdin.readline())
for i in range(1, N+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq[0])