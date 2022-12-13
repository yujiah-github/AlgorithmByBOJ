import heapq,sys

N = int(sys.stdin.readline())

heap_list = []

for n in range(N):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(heap_list, (abs(x),x))
        
    else:
        if len(heap_list) == 0:
            print(0)
        
        else:
            t = heapq.heappop(heap_list)
            print(t[1])
    