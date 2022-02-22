nums = list(map(int,input().split()))
while True:
    if nums[0]== 1:
        if nums[1] == 2:
            print("ascending")
        else:
            print("mixed")
    elif nums[0] == 8:
        if nums[1] == 7:
            print("descending")
        else:
            print("mixed")
    else:
        print("mixed")