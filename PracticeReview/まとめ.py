
#2609番
import sys,math
x,y = map(int, sys.stdin.readline().split())
print(math.gcd(x,y))
print(math.lcm(x,y))

#11050
import sys,math

N,K = map(int, sys.stdin.readline().split())
print(math.comb(N,K))