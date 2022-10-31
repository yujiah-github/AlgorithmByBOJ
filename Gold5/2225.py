import sys

n, k = map(int, sys.stdin.readline().split())
mod = 1000000000
tbl = [1]
tbl += [0] * n

for _ in range(1, k+1):
    for idx in range(1, n+1):
        tbl[idx] = (tbl[idx] + tbl[idx-1])%mod

sys.stdout.write(str(tbl[n]))