import sys
from itertools import combinations

dwarf = [int(sys.stdin.readline()) for d in range(9)]

for combi in combinations(dwarf, 7):
    if sum(combi) == 100:
        ans = list(combi)
        break
        
for a in sorted(ans):
    print(a)