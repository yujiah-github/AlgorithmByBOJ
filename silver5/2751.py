n = int(input())
list_n = []
for i in range(n):
    list_n.append(int(input()))
list_n.sort()
for i in range(n):
    print(list_n[i])