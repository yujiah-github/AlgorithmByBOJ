n = int(input())
list_a = list(map(int, input().split()))
maximum = max(list_a)

new_list = []
for score in list_a:
    new_list.append(score / maximum * 100)
avg = sum(new_list) / n
print(avg)