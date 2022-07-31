import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

x = a1 * b2 + a2 * b1
y = b1 * b2

c = math.gcd(x, y)
x //= c
y //= c

print(x, y)