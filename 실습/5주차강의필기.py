#### 5주차 1 ####
# A = input()
# escape 문자 

# print("정신차려\n"+"이친구야")
# print("정신차려\n이친구야")
# print("\"정신차려\"\n이친구야")

# print("\n"*10+"이친구야")

# # 스트링 출력 포맷
# phi = 3.14
# x = 3
# y = 4

# # print("Phi is %d" %phi)
# # print("x is %d, y is %d " %(x,y))
# # print("Hello, %s" %input())

# # WWW 으로 부터의 입력 ??? 

# # 랜덤난수
# import random
# i = 1 

# for i in range(1,6):
#     print("Random #%d : %d " %(i, random.randint(1,6)))
#     i += 1

# 숙제 로또 만들기

#### 5주차 2 ####

# print(bool(3>4))
# print(bool(3==4))
# print(bool(3<=4))

# 윤년 판별
# 4로 나누어지는 해는 윤년이다
# 그러나 100으로 나누어지는 해는 윤년이 아니다
# 그러나 400으로 나누어지는 해는 다시 윤년이다.

year = int(input("년도를 입력하세요:"))

if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 ==0 )):
    print("yes") 
else:
    print("no")

################################## 5주차 3 ##################################

for name in ["철수","영희","길동","영진"]:
    print("안녕")

# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x, end='')  #한 줄로 쓰고싶다면 end =''

# range() 함수 특정 구간의 정수

sum = 0
for x in range(10):
    sum += x
print(sum)

# range(start,stop,step)

for c in "abcdef":
    print(c, end=" ")

n = int(input("어디까지?: "))
for i in range(n):
    i += i
print(i)


for t in range(0,100+1,10):
    c =(t-32.0) * 5.0/9.0
    print(t,"->",round(c,2))

###   round(A,2) A를 둘째자리까지 반올림 

## turtle 그려보기 ###  ???????????

##############################  5주차 4 ###################################### 
# while 조건 : 

i = 0  # while 전 초기값 설정필요
while i < 5 : 
    print("환영합니다")
    i += 1
print("반복이 종료되었습니다.")

## 보초값 사용하기 (sentinel) ##
