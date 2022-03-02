import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
num_list = []
while M<N+1:
    for i in range(2,M):
        if M%i == 0:
            break
    num_list.append(M)
    i += 1
M += 1

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))