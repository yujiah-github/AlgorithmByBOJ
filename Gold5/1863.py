import sys;
def main():
    N = int(sys.stdin.readline())
    building = [0]
    answer = 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())

        if y > building[-1]:
            answer += 1
            building.append(y)
        else:
            while building[-1] > y:
                building.pop()

            if building[-1] < y:
                answer += 1
                building.append(y)
    print(answer)


if __name__ == '__main__':
    main()