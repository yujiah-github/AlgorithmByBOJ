n, x, y = map(int, input().split())
count = 0
while x != y:
    x -= y// 2
    x -= y // 2
    count += 1
print(count)