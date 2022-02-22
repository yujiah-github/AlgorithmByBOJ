cnt = 0
list_n2 =[]
while cnt<10:
    n1 = int(input())
    n2 = n1 % 42
    list_n2.append(n2)
    cnt += 1
s1 = set(list_n2)
print(len(s1))