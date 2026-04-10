import sys

def canndy(board):
    m,n=len(board),len(board[0])
    stack=[]

    

    while True:
        if m>=3:
        #todo:标记横向
            for i in range(m):
                stack.append(board[i][0])
                stack.append(board[i][1])
                for j in range(2,n):
                    if abs(stack[j-1])==abs(stack[j-2])==abs(stack[j])!=0:
                        board[i][j],board[i][j-1],board[i][j-2]=-stack[j],-stack[j-1],-stack[j-2]
                        #识别到三个相同的元素，出栈
                        k=j+1
                        while k<n:
                            if stack[k]==stack[j]:
                                board[i][k]=-stack[k]
                                K+=1
                            else:
                                break
                    



        # todo:标记纵向


        #todo:判断是否消除完毕
        if changed:
            #todo: 发生改变，进行下落
            pass
        else:
            return 




    
