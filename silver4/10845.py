from collections import deque
import sys
queue = deque()
N = int(sys.stdin.readline())
for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        queue.append(command[1])
    
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            left_num = queue.popleft()
            print(left_num)
           
    elif command[0] == 'size':
        size_num = len(queue)
        print(size_num)
        
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    else:
        if len(queue) == 0:
            print(-1)
        else:
            num = len(queue) - 1
            print(queue[num])