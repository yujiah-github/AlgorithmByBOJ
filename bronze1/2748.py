n = int(input())
list = [0 , 1]
for i in range(n-1):
    nextValue = list[i] + list[i+1]
    list.append(nextValue)

print(list[n])