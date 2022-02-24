import math
x, y, z = map(int,input().split())
n = math.ceil((z-y) /(x - y))
print(n)