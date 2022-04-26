import sys
s = int(sys.stdin.readline())
sum = 0
i = 1
while True:
    sum += i
    if sum > s:
        break
    i += 1
    
print(i-1)