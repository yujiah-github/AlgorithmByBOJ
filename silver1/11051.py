import math
a, b = map(int,input().split())
n = math.comb(a,b)
print(n % 10007)