cnt = 0
while cnt<9:
     numbers = list(map(int, input().split()))
     cnt += 1
print(max(numbers))
print(min(numbers))