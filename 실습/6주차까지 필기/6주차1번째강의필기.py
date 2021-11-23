#########################  6주차 1 ############################# 

#for loop 이나 while loop이 끝나기 전에 빠져나오고 싶을 때

# for i in range(1,7):
#     print()
#     print('i = ', i, end=" ")
#     print('Hello, how', end=' ')
#     if i ==3 :
#         continue    # continue는 밑에 명령어를 실행시키지 않고 다시 반복
#     print('r u?')



# for i in range(1,7):
#     print()
#     print('i = ', i, end=" ")
#     print('Hello, how', end=' ')
#     if i ==3 :
#         break     # break은 밑에 명령어 실행시키지 않고 아예 반복 종료
#     print('r u?')   

# 유클리드 알고리즘
# 최대공약수 구하기 !!!! 
# 40=(2*2*2*5) 와 24=(2*2*2*3) 의 최대공약수 = 8(2*2*2)
# 정수 a 와 b 의 최대공약수 (a>= b>0)를 G(a,b)라고 하면

# if b == 0 면 종료 , a가 최대 공약수
# a=b ,b=a%b
# 1,2 반복

a= int(input("A :")) ; b= int(input("B:"))
while (b != 0) :
    x=a
    a=b
    b=x%b
    # a,b=b,a%b       #이런식으로 간단하게 만들 수도 있다.
print("GCD is %d" %a)


# 요일 구하는 프로그램 !!!!!!!!! 중요
# 1년 1월 1일은 월요일이므로 날짜수
# 윤년일때는 366일 윤년이 아닐 때는 365일

# year = int(input("년도는 ? : "))
# month = int(input("월은 ? : "))
# date = int(input("일은 ? : "))
# yearday = 0
# monthday = 0
# dateday = 0

# for i in range(1,year):
#     if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0 :
#         day = 366
#         yearday += day
                
#         for j in range(1,month):
#             if j in [1,3,5,7,8,10,12]:
#                 day = 31
#                 monthday += 31
#             elif j in [4,6,9,11]:
#                 day =30
#                 monthday += 30
#             else : 
#                 day =29
#                 monthday += 29

#     else :
#         day = 365
#         yearday += day

#         for j in range(1,month):
#             if j in [1,3,5,7,8,10,12]:
#                 day = 31
#                 monthday += 31
#             elif j in [4,6,9,11]:
#                 day =30
#                 monthday += 30
#             else : 
#                 day =28
#                 monthday += 28

# result = yearday + monthday + date-1

# if result % 7 == 0 :
#     print("Monday")
# elif result % 7 == 1 :
#     print("Tuseday")
# elif result % 7 == 2 :
#     print("Wednesday")
# elif result % 7 == 3 :
#     print("Thursday")
# elif result % 7 == 4 :
#     print("Friday")
# elif result % 7 == 5 :
#     print("Saturday")
# elif result % 7 == 6 :
#     print("Sunday")

# print(yearday,monthday,date-1,result)

