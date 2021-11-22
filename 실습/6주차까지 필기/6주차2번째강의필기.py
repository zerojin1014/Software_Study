#########################  6주차 2 ############################# 

# 곱셈표 출력
# n= int(input("몇 단? : "))
# for multi in range(1,10):
#     print(n,"x",multi,"=",n*multi)

# 4단부터 6단까지 곱셈표
for n in range(4,7):
    for multi in range(1,10):
        print(n,"x",multi,"=",n*multi)
    print()

#nested for loop 문법
for i in range(10):
    for j in range(10):
        print("*", end='')
    print("")

i = 0
while (i < 10):
    j = 0
    while (j < 10):
        print("*",end="")
        j += 1
    i += 1
    print("")

# 구구단 출력 For loop > while loop
# 삼각형 출력 주어진 n에 따라 높이가 n인 직각 삼각형 출력

# 소수판별 
# 주어진 수 p가 1과 자신만으로 나누어지는 수 인지 판별하는 프로그램
# 이중 loop 사용하고, 반복횟수를 p/2 보다 적게하시오
# 힌트 python 제곱근 함수 사용법
import math as m
n =10
print(m.sqrt(n))

# n이 소수가 아니면 n은 sqrt(n) 이하의 숫자들을 약수로 갖는다.

#조화급수와 로그....

