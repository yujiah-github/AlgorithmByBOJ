import sys

n = int(sys.stdin.readline())

lst = []
lst_dict = {}
numList = []

for i in range(n):
    lst.append(sys.stdin.readline().rstrip())

for i in range(n): 
    for j in range(len(lst[i])): 
        if lst[i][j] in lst_dict: 
            lst_dict[lst[i][j]] += 10 ** (len(lst[i])-j-1)
        else:
            lst_dict[lst[i][j]] = 10 ** (len(lst[i])-j-1)

for val in lst_dict.values():
    numList.append(val)

numList.sort(reverse=True)

sum = 0
pows = 9
for i in numList: 
    sum += pows * i
    pows -= 1

print(sum)