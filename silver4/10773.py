import sys
n = int(sys.stdin.readline())
stack = []
sum = 0
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        sum = sum - stack[len(stack)-1]
        stack.pop()
    else:
        stack.append(x)
        sum += x
print(sum)