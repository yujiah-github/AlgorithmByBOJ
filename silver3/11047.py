import sys
N,K = int((sys.stdin.readline().split()))
M_list = []
for i in range(N):
    M = int(sys.stdin.readline())
    M_list.append(M)
S_list = []
while True:
    for i in range(N):
        if K / M_list[N-i] == 0:
            continue
        else:
            S = K/M_list[N-i]
            S_list.append(S)
            cnt= K - (S * M_list[N-i])
print(sum(S_list))