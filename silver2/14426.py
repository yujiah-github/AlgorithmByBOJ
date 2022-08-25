from sys import stdin

N,M = map(int,stdin.readline().rstrip().split())
S = [stdin.readline().rstrip() for _ in range(N)]
T = [stdin.readline().rstrip() for _ in range(M)]

dic = {}

for s in S:
    for i in range(1,len(s)+1): dic[s[:i]] = 1

cnt = 0
for t in T:
    try:
        cnt += dic[t]
    except KeyError:
        pass

print(cnt)