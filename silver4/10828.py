import sys
n = int(sys.stdin.readline()) #명령 숫자 입력 받기
lst = [] #명령어를 저장할 리스트
for i in range(n): #입력 받은 숫자만큼 반복
    commend = sys.stdin.readline().split() # commend에서 명령어와 숫자를 받음
    if commend[0] == 'push': #명령어가 push인 경우
        lst.append(commend[1]) #명령어가 push라면 lst[1]의 수를 리스트에 추가
    
    elif commend[0] == 'pop': #명령어가 pop인 경우
        if len(lst) == 0:
            print(-1)
        else: 
            x = lst.pop() #리스트에서 가장 위에 있는 숫자 빼기
            print(x) #가장 위에 있던 숫자 출력
    
    elif commend[0] == 'size': #명령어가 size인 경우
        print(len(lst))  #리스트의 크기 반환
    
    elif commend[0] == 'empty': #명령어가 empty인 경우
        if len(lst) == 0: #리스트가 비어있으면 1을 반환
            print(1)
        else:
            print(0)
            
    elif commend[0]== 'top': #명령어가 top인 경우
        if len(lst) == 0: #리스트가 비어있으면 -1을 반환, 아닐 경우 가장 끝 수를 반환
            print(-1)
        else:
            print(lst[-1])