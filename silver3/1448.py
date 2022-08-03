import sys
x = int(input())
y = []
for i in range(t):
    y.append(int(sys.stdin.readline()))
y.sort(reverse=True)
istrue = False
for i in range(len(s) - 2):
    if y[i] < y[i + 1] + y[i + 2]:
        print(y[i] + y[i + 1] + y[i + 2])
        istrue = True
        break
if istrue == False:
    print(-1)