#########################  6주차 2 ############################# 

# 곱셈표 출력
# n= int(input("몇 단? : "))
# for multi in range(1,10):
#     print(n,"x",multi,"=",n*multi)

# 4단부터 6단까지 곱셈표
'''
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
'''

# 구구단 출력 For loop > while loop
# 삼각형 출력 주어진 n에 따라 높이가 n인 직각 삼각형 출력

# 소수판별 
# 주어진 수 p가 1과 자신만으로 나누어지는 수 인지 판별하는 프로그램
# 이중 loop 사용하고, 반복횟수를 p/2 보다 적게하시오
# 힌트 python 제곱근 함수 사용법
import math as m
from datetime import datetime

def is_real_number(x):
    
    count =0
    
    for num in range(2,x+1):
        divisor = 0

        for i in range(2,int(m.sqrt(num))+1):
            if num % i == 0 :
                divisor = 1
                break

        if divisor == 0:
            count += 1

    return count

start =datetime.now()
print(is_real_number(10000)) 
end = datetime.now()
print('걸린 시간 : ',end-start) # 현재 시간 - 함수 시작 시간


'''
from datetime import datetime

num =int(input("정수를 입력하세요 : "))
prime_num = []

for n in range(2,num+1):
    divisor = 0
    if n <= 1:
        False
    for x in range(2,n):
        if n % x == 0 :
            divisor = 1
            break
    if divisor == 0 :
        prime_num.append(n)

start =datetime.now()

print("소수의 개수는", len(prime_num)," 개 입니다.")
print("소수는", prime_num)

end = datetime.now()
print('걸린 시간 : ',end-start) # 현재 시간 - 함수 시작 시간

'''


        # for i in range(2,int(m.sqrt(num))+1):
        #     if num % i == 0:
        #         return False    #소수가 아님

# import math as m
# n =10
# print(m.sqrt(n))

# n이 소수가 아니면 n은 sqrt(n) 이하의 숫자들을 약수로 갖는다.

#조화급수와 로그....

