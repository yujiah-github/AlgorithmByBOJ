import math
import sys
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
first_n = list_n[0]
for i in range(1,n):
    s = math.gcd(first_n,list_n[i])
    print('{0}/{1}'.format(first_n//s, list_n[i]//s))