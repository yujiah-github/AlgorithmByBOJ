num_list = []

for i in range(9):
    N = int(input())
    num_list.append(N)

print(max(num_list))
print(num_list.index(max(num_list))+1)