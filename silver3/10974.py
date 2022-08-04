n = int(input())
x = []

def dfs():
    if len(x) == n:
        print(*x)
        return
    for i in range(1, n + 1):
        if i not in x:
            x.append(i)
            dfs()
            x.pop()

dfs()