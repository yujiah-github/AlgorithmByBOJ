from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N + 1)])
result = ['<']

while True :
    queue.rotate(-K)
    if len(queue) > 1 :
        result.append(str(queue.pop()) + ', ' )
    
    elif len(queue) == 1 :
        result.append(str(queue.pop()) + '>')
        break

result = ''.join(result)
print(result)