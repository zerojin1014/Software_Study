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
    # x=a
    # a=b
    # b=x%b
    a,b=b,a%b       #이런식으로 간단하게 만들 수도 있다.
print("GCD is %d" %a)

# 요일 구하는 프로그램 !!!!!!!!! 중요
# 1년 1월 1일은 월요일이므로 날짜수
# 윤년일때는 366일 윤년이 아닐 때는 365일