import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
a.sort()
gap_list = []
for i in range(n-1):
    j= i + 1
    for j in range(n):
        gap = a[j]-a[i]
        gap_list.append(gap)
gap_lst = list(set(gap_list))
min_gap = min(gap_lst)
min_gap_cnt = gap_list.count(min_gap)
print(min_gap, min_gap_cnt)

