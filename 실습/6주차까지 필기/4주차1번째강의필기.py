#######################  4주차 1 #############################

# if else문

# 관계 연산자
# x == y , x != y, x>=y, x<=y 

# 순서도 그리기                                 # 공부 필요 (중간고사)
# 터틀 그래픽

# import turtle
# t = turtle.Pen()
# direction = str()

# while True:
#     direction == input("왼쪽 = left, 오른쪽 = right : ")
#     if direction == "left":
#         t.left(60)
#         t.forward(50)
#     elif direction == "right":
#         t.right(60)
#         t.forward(50)

# 짝수인지 홀수인지 

A = int(input("정수를 입력하세요:"))
if A % 2 == 0 :
    print("짝수입니다.")
elif A % 2 == 1 :
    print("홀수 입니다.")
else :
    print("0입니다.")

# 문자열의 중간문자 찾기

string = input("문자열을 입력하세요: ")
length = len(string)

if length%2 == 1:  # 문자개수가 홀수
    ch1 = string[length//2]   #abcde 중에 5//2 = 2 index[2] = c
    print("중앙 글자는 ", ch1)

else: #abcd 중에 bc, 인덱스로는 1,2번째 4//2 와 4//2 -1
    ch1 = string[length//2-1]
    ch2 = string[length//2]
    print("중앙 글자는" , ch1,',',ch2)

