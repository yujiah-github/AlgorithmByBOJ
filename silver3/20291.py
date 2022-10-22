def file_clean(n):
    ans = {}
    for _ in range(n):

        split = input().split(".")[1]
        ans.setdefault(split, 0)
        ans[split] += 1

    for k, v in sorted(ans.items(), key=lambda x: x[0]):
        print(k, v)

n = int(input())
file_clean(n)