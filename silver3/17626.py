import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)
d[0], d[1] = 0, 1

for i in range(2, n + 1):
    min_value = 1e9
    j = 1
    while (j ** 2) <= i:
        min_value = min(min_value, d[i - (j ** 2)])
        j += 1
    d[i] = min_value + 1

print(d[n])