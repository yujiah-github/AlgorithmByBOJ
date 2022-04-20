import sys
c = int(sys.stdin.readline()) #테스트 케이스 입력

for i in range(c): #c만큼 입력 받아야하므로
    a = list(map(int, sys.stdin.readline().strip().split()))
    avg = sum(a[1:]) / a[0]
    cnt = 0

    for score in a[1:]:
        if score > avg:
            cnt += 1
             
    result = (cnt / a[0]) * 100
    print(f'{result:.3f}%')