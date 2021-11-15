# Tic Tac Toe 게임은 3 by 3 보드에 두 player가 번갈아 가면서
# 말을 놓아서, 순차적으로 3개의 말을 보드 위에 나열하면 이기는
# 게임이다
# 
# 보드를 2차원 리스트로 만든 후, 각 element에 한 개의 빈 문자를 넣어서
# 초기화를 합니다.
# 그 2차원 리스트에, 한 명의 player가 순차적으로 말을 놓은 것인지
# 확인하는 function을 만들어주세요.

# 초기화된 2차원 리스트 보드는 다음과 같습니다.
# [['','',''],['','',''],['','','']]

# 'X'가 이기는 경우는 같은 행 3개
# [['X','X','X'],['','',''],['O','O','']

# 같은 열 3개
# ['X','','O']
# ['X','','']
# ['X','O','']]

# 대각선의 순차적 3개 (기울기가 양과 음)
# [['X','','O'],['','X',''],['','O','X']]s
# [['','','X'],['O','X',''],['X','','O']]

# 첫번째 parameter는 , 2차원 보드
# 두번째 parameter는 문자 (예를 들어서 'X'나 'O')
# 세번째 parameter는 x 좌표 (0,1,2 중 하나이며 행의 값)
# 네번째 parameter는 y 좌표 (0,1,2 중 하나이며 열의 값)

# 이기면 True 값을 return 하고
# 이기는 3개의 순차적 문자 elements 가 없으면 False 값을 return 하시오.FileNotFoundError

# (단 프로그래머스쿨의 제한적인 상황으로 인하여, 실제 코드에서는 문자가 아닌 string타입이며,
#  두번째 parameter 도 문자가 아닌 string 입니다.)


# def solution(gameboard, ch, x, y):
#     answer = False
#     return answer

def drawBoard(board):
    print("     0  |  1 |  2 ")
    print("    ----|----|----")
    for r in range(3) :
        print(r, ":   " + board[r][0] + " |  " + board[r][1] + " |  " + board[r][2])
        if (r != 2) :
            print("    ----|----|----")

def checkToWin(board, ch, x, y):

    if board[x][0] == board[x][1] == board[x][2] == ch :
        return True

    elif board[0][y] == board[1][y] == board[2][y] == ch:
        return True
    
    elif board[0][0] == board[1][1] == board[2][2] == ch:
        return True

    elif board[2][0] == board[1][1] == board[0][2] == ch:
        return True
         
    else :
        return False

##########################################################
import random
print("TicTacToe Game 을 시작합니다.")
board = [[' ' for x in range(3)] for y in range(3)]
#empty board
print(board)
turn = 0 

while True : 
    
    turn += 1
    drawBoard(board)
    
    # 사용자로부터 좌표를 입력받는다.
    x = int(input("행의 x좌표를 입력하시오 (0,1,2): "))
    y = int(input("열의 y좌표를 입력하시오 (0,1,2): "))
    print("(x,y) = (",x, ",",y, ") 에 X 표를 합니다. \n")
    
    # 사용자가 입력한 좌표를 검사한다.
    if board[x][y] != ' ':
        print("잘못된 위치입니다. ")
        continue
    else : 
        board[x][y] = 'X'
        
        
    # # 컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    # done = False
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] == ' ' and not done:
    #             board[i][j] = 'O'
    #             done = True
    #             break
            
    # 사용자가 이겼는지 확인합니다. 이긴 경우 while loop를 종료합니다.
    if (checkToWin(board, 'X', x, y) == True):
        print("이겼습니다!! 축하합니다.")
        drawBoard(board)
        break

    if turn >= 5 :
        drawBoard(board)
        break    

    # 컴퓨터가 놓을 위치를 random 으로 결정한다.
    
    locating = True 
    while locating:
        com_x = random.randint(0,2)
        com_y = random.randint(0,2)
            
        if board[com_x][com_y] == ' ':
            board[com_x][com_y] = 'O'
            locating = False
           
    # 컴퓨터가 이겼는지 확인합니다. 사용자가 진 경우도 while loop를 나갑니다.
    if (checkToWin(board, 'O', com_x, com_y) == True ):
        print("컴퓨터가 이겼습니다.. 안타깝네요")
        drawBoard(board)
        break
    
    if turn >= 5 :
        break
print("Game over!")


# while True :
#      # 게임 보드를 그린다.
#      for i in range(3):s
#          print(" " + board[r][0]+"| "+ board[r][1]+"| " + board[r][2])
         
#          if(r != 2):
#              print("---|---|---")
             
#                 #사용자로부터 좌표를 입력받는다.
#     x = int(input("다음 수의 x좌표를 입력하시오 : "))
#     y = int(input("다음 수의 y좌표를 입력하시오 : "))