import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n) :
  data.append(n)

data.sort(reverse=True)

result = 0
for i in range(n) :
  value = data[i] - ((i+1)-1)
  if value > 0 :
    result += value

print(result)