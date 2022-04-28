import sys
N = int(sys.stdin.readline())
cute = not_cute = 0
for i in range(N):
    if int(sys.stdin.readline()) == 1:
        cute += 1
    else:
        not_cute += 1
print("Junhee is cute!" if cute > not_cute else "Junhee is not cute!")