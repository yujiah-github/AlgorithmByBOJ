import sys

n = int(sys.stdin.readline())
lines = []

for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort()

x = lines[0][0]
y = lines[0][1]
ans = 0

for i in range(1, n):
    if y >= lines[i][1]:
        continue
    
    elif lines[i][0] <= y < lines[i][1]:
        y = lines[i][1]
    
    elif y < lines[i][0]:
        ans += y - x
        x = lines[i][0]
        y = lines[i][1]

ans += y - x
print(ans)