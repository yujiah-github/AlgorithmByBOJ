import sys

N = int(sys.stdin.readline())
total_people = 0
houses = []

for _ in range(N):
    X, A = map(int, sys.stdin.readline().split())
    total_people += A
    houses.append((X, A))

peopleCount = 0
for X, A in sorted(houses, key = lambda x: x[0]):
    peopleCount += A
    if peopleCount > total_people//2:
        print(X)
        break