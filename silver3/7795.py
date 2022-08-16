import bisect, sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    count = 0
    for a in A:
        count += (bisect.bisect(B, a-1))
    print(count)