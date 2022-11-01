import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    min_lst = []
    if n == 1:
        arr.sort()
        for i in range(5):
            ans += arr[i]
    else:
        min_lst.append(min(arr[0], arr[5]))
        min_lst.append(min(arr[1], arr[4]))
        min_lst.append(min(arr[2], arr[3]))
        min_lst.sort()

        min1 = min_lst[0]
        min2 = min_lst[0] + min_lst[1]
        min3 = sum(min_lst)

        n1 = 4 * (n - 2) * (n - 1) + (n - 2) ** 2
        n2 = 4 * (n - 1) + 4 * (n - 2)
        n3 = 4

        ans += min1 * n1
        ans += min2 * n2
        ans += min3 * n3
    print(ans)