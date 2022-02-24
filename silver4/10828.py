import sys
n = int(sys.stdin.readline()) #명령의 수 입력
stack = [] #리스트 생성
for i in range(n):
    x = sys.stdin.readline().split() #명령어와 숫자 입력
    
    if x[0] == 'push': #명령어가 푸쉬인 경우
        stack.append(x[1]) #list_num에 추가 (입력값이 명령어와 숫자로 구성되어 있으므로 인덱스는 0과 1밖에 없다)
    
    elif x[0] == 'pop': #명령어가 팝인 경우
        if len(stack) == 0:
            print(-1) #정수가 없으면 -1을 출력
        else:
            print(stack.pop()) #제거
            
    elif x[0] == 'size': #명령어가 size인 경우
        print(len(stack))
    
    elif x[0] == 'empty': #empty인 경우
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif x[0] == 'top':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1]) 