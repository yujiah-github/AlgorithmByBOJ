import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    c = [str(sys.stdin.readline().strip()) for _ in range(n)]
    c.sort()
    check = "yes" 

    for i in range(len(c) - 1):
        if c[i] == c[i + 1][0:len(c[i])]:
            check = "no"

    if check == "no":
        print("NO")
    else:
        print("YES")