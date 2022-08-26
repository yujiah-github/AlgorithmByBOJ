import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

min_count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - N) + len(nums))

print(min_count)