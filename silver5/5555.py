import sys
fw = sys.stdin.readline().replace("\n","")
n = int(sys.stdin.readline())

def finds(fw, word):
    ans = 0
    if word.find(fw) >= 0:
        ans = 1
    for i in range(len(fw)):
        word = word[-1] + word[0:len(word)-1]
        if word.find(fw) >= 0:
            ans = 1
            break
    return ans

real_ans = 0
for _ in range(n):
    word = sys.stdin.readline().replace("\n", "")
    real_ans += finds(fw,word)
print(real_ans)