a,b = map(int,input().split())
re_a = int(str(a)[::-1])
re_b = int(str(b)[::-1])
if re_a > re_b:
    print(re_a)
else:
    print(re_b)