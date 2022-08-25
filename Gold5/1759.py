import sys

def backTraking(cnt, idx):
    if cnt == l:
        vo, co = 0, 0
        for i in range(l):
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(words[i])
        backTraking(cnt + 1, i + 1)
        answer.pop()


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
backTraking(0, 0)