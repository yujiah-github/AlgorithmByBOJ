n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)

#문제 해결은 했으나 문제에서 원하는 조건을 맞추진 못함. 나중에 다시 풀어볼 것.