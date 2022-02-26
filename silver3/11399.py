from re import S
import sys
n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
sum =0

for i in range(1,n):
    num_list[i] += num_list[i-1]

print(sum)