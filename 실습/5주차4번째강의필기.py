##############################  5주차 4 ###################################### 
# while 조건 : 

# i = 0  # while 전 초기값 설정필요
# while i < 5 : 
#     print("환영합니다")
#     i += 1
# print("반복이 종료되었습니다.")

## 보초값 사용하기 (sentinel) ##

# i = 0
# while i < 10:
#     print(i, end='')
#     i += 1

# 팩토리얼 계산 

# num = int(input())
# i = 1
# sum = 1

# while i <= num :
#     sum *= i
#     i += 1
# print(num,"! 는 %d 입니다." %sum)

# 구구단 출력 

# num = int(input())
# i = 1

# while i <= 9 :
#     print(num,"*",i,"= %d" %(num*i))
#     i += 1

# 배수의 합 계산 프로그램
# 1과 100사이의 모든 3의 배수의 합
# i=1
# sum = 0

# while i <= 100 :
#     if i % 3 == 0:
#         sum += i
#     i += 1
# print(sum)

# 자리수의 합
# 각 자리수의 합을 계산하는 프로그램을 작성해보자
# 1234 라면 (1+2+3+4)를 계산하는 것이다.

# num = int(input())
# other = 0
# sum = 0

# while num > 0 :
#     other = num % 10
#     sum += other
#     num = num//10
# print(sum)

#보초값 (sentinel) 사용하기
#사용자로부터 임의의 개수의 성적을 받아서 평균을 계산한 후에
#출력하는 프로그램을 작성하여 보자. 센티널로는 음수의 값을 사용하자.
# score = 1
# i = 0
# sum = 0

# while score >= 0 :
#     score = float(input("성적을 입력하세요 : "))
#     if score > 0 :
#         sum += score
#         i += 1

# if i > 0 :
#     print("성적의 평균은 %f 입니다." %(sum/i))

## %d는 정수(integer) %s는 문자열(string) %f는 실수(float)

# 숫자 맞추기 게임