n = int(input())
num = int(input())
x = [int(a) for a in str(num)]
sum =0
i =0
while i<n:
    sum += x[i]
    i += 1
print(sum)
