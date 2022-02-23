nums = list(map(int, input().split()))
nums_sort = nums.sort()
nums_reverse = nums_sort.reverse()
while True:
    if nums == nums_sort:
        print("ascending")
    elif nums == nums_reverse:
        print("descending")
    else:
        print("mixed")