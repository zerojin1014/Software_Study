#### 5주차 2 ####

# print(bool(3>4))
# print(bool(3==4))
# print(bool(3<=4))

# 윤년 판별
# 4로 나누어지는 해는 윤년이다
# 그러나 100으로 나누어지는 해는 윤년이 아니다
# 그러나 400으로 나누어지는 해는 다시 윤년이다.

# year = int(input("년도를 입력하세요:"))

# if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 ==0 )):
#     print("yes") 
# else:
#     print("no")

# ################################## 5주차 3 ##################################

for name in ["철수","영희","길동","영진"]:
    print("안녕,",name)  

# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x, end='')  #한 줄로 쓰고싶다면 end =''

# range() 함수 특정 구간의 정수

# sum = 0
# for x in range(10):
#     sum += x
# print(sum)

# # range(start,stop,step)

# for c in "abcdef":
#     print(c, end=" ")
sum = 1
n = int(input("어디까지?: "))
for i in range(1,n+1):
    sum *= i
print(sum)


for t in range(0,100+1,10):
    c =(t-32.0) * 5.0/9.0
    print(t,"->",round(c,2))

###   round(A,2) A를 둘째자리까지 반올림 

## turtle 그려보기 ###  ???????????
import turtle

polygon = turtle.Turtle()

for i in range(5): 
    polygon.forward(50)
    polygon.right(144)

import math
t = turtle.Turtle()

t.pendown()
for angle in range(360):
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 200 
    t.goto(scaledX,scaledY)
t.penup()
