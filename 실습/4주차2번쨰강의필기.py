#######################  4주차 2 #############################

# 1 = ture , 0 = false
# 논리 연산자
# x and y : x와 y가 모두 참이면 참 그렇지 않으면 거짓
# x or y : x 나 y 중에서 하나만 참이면 참 모두 거짓이면 거짓
# not x : x가 참이면 거짓, x가 거짓이면 참
 
# 연속적인 if-else 문
# 학생들의 성적을 받아서 90점 이상이면 A 80점 이상이면 B 80미만이면C

# for i in range(1,4):
#     score = int(input("시험점수를 입력해주세요 : "))
#     if score >= 90 :
#         print (i,"번째 학생은 A입니다.")
#     elif score >= 80 : 
#         print (i,"번째 학생은 B입니다.")
#     else : 
#         print (i,"번째 학생은 C 입니다.")


# 아이디를 입력받아서 등록된 아이디인지 검사하는 프로그램
# 등록된 아이디를 리스트(list)에 저장하도록 한다. 아이디가 일치하면 패스워드 물어본다.

# print("회원가입 창입니다.")
# IdList = []
# Id = input("원하는 아이디를 입력하세요:")
# IdList.append(Id)
# print(IdList)

# Id = input("아이디를 입력하시오: ")

# if Id in IdList:
#     passWord= input("패스워드를 입력하시오: ")
#     if passWord == "123456":
#         print("환영합니다!")
#     else :
#         print("잘못된 패스워드입니다.")

# else :
#     print("등록되지 않은 회원입니다.")

######### 윤년 판단하기 ##################
# 윤년의 조건 
# 연도가 4로 나누어 떨어지면 윤년이다. 그치만 100으로 나누어 떨어지는 연도는 제외한다.
# 다시 400으로 나누어 떨어지면 윤년이다.
# 윤년은 2월에 하루가 더해져서 29일 까지 있습니다.

year = int(input("연도를 입력하세요 : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print("윤년입니다.") 
else :
    print("윤년이 아닙니다.")

# 근의 공식 x = [-b +- sqrt(b**2 -4*a*c)/2*a]

# 숫자게임에 오신걸 환영합니다. 
# Random Module 

# seed() : Initialze the random number generator
# randint() : Returns a random number between the given range
# choice() : Returns a random element from the given sequence
# random() : Returns a random float number between 0 and 1


#### 4주차 3 #### (Revisit)
# 컴퓨터는 정보를 비트로 표시
# 8비트 -> 1바이트 , 32/64 비트 -> 1워드(word)

# 비트 논리 연산자 ????????                 >> 공부필요
# 비트 쉬프트 연산자 ??
# 비트마스크 ??

# E - 표기법 ??
# 10진수 -> 2진수 변환 ?

#### 4주차 4 ####

string ='abcdef'
print(string[0:4])

# string[3] = 'z'  >>>>>>> string은 불변 타입 immutable 

# 불변 데이터 타입 : tuple , string
# 가변 데이터 타입 : list , dictionary, set

# Boolean Data > True 는 1 False는  0   bool() : boolean으로 변환
# chr(숫자) : 숫자에 해당하는 아스키 (ascii) 문자로 변환
# ord(문자) : 아스키 문자에 해당하는 숫자로 변환
# Type() : 변수가 가리키는 객체 (object)의 타입을 알고 싶을 때 사용함

