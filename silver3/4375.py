def solution(n) :
  count = 1
  div = 1
  while True :
    if count == 1 : left = div%n
    else : left = ((div%n)*(10%n)+1)%n
    
    if left == 0 : return count
    else :
      div = left
      count += 1

while True :
  try :
    n = int(input())
    print(solution(n))
  except :
    break