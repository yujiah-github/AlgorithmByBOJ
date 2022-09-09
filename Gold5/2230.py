import sys

if  __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    arr = [0] * a
    for i in range(N):
        arr[i] = int(sys.stdin.readline().rstrip())
    arr.sort()
    left, right = 0, 1
    ans = sys.maxsize

    while left < a and right < a:
        tmp = arr[right] - arr[left]
        if tmp == b:
            print(b)
            exit(0)
        if tmp < b:
            right += 1
            continue
        left += 1
        ans = min(ans, tmp)
    print(ans)