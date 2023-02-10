#4153番
import sys

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if sum(num_list) == 0:
        break
    max_number = max(num_list)
    num_list.remove(max_number)
    if num_list[0] ** 2 + num_list[1] ** 2 == max_number ** 2:
        print("right")
    else:
        print("wrong")

#1259番
while True:
    n = input()
    if n == "0":
        break
    elif n == n[::-1]:
        print("yes")
    else:
        print("no")


#2609番
import sys,math
x,y = map(int, sys.stdin.readline().split())
print(math.gcd(x,y))
print(math.lcm(x,y))

#11050番
import sys,math

N,K = map(int, sys.stdin.readline().split())
print(math.comb(N,K))