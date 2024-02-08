stack=[]
while True:
    select=int(input('1:삽입, 2:삭제, 3:종료 '))
    if select==1:
        data=int(input('삽입할 데이터: '))
        stack.append(data)   # 용량의 제한이 없는 버전
        print(stack)
    elif select==2:
        if len(stack)==0:
            print('스택이 비었습니다.')
        else:
            data=stack.pop()
            print('삭제된 데이터:', data)
            print(stack)
    else:
        break
