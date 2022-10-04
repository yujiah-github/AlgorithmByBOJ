def file_clean(n):
    ans = {}
    for _ in range(n):

        # 입력받은 문자에서 확장자만 저장하자.
        split_s = input().split(".")[1]

        # 확장자가 없으면 0으로 초기화한 후 1 더하고, 있으면 그냥 1 더하자.
        ans.setdefault(split_s, 0)
        ans[split_s] += 1

    # 확장자 오름차순 정렬
    for k, v in sorted(ans.items(), key=lambda x: x[0]):
        print(k, v)


n = int(input())
file_clean(n)