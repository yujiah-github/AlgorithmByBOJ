n = int(input())
list = []
for i in range(n):
    list.append(str(input()))
if list == sorted(list, reverse=True):
    print('DECREASING')
elif list == sorted(list):
    print('INCREASING')
else:
    print('NEITHER')