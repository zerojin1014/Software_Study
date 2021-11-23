# 라코테 2번 문제

'''
주어진 수의 범위 내에서 prime 수의 개수를 세시오.
prime은 소수이며, 1과 그 수 자신 이외의 자연수로는 나눌 수 없는, 1보다 큰 자연수를 말한다.
주어지는 같은 범위 값을 알려주고 있으며, 1부터 그 범위 안에 있는 prime인 수의 갯수를 세서 만드시오

예 1) 주어진 수가 10이면 prime 수가
2, 3, 5, 7
이므로 4를 return 한다.

예 2) 주어진 수가 13이면 prime 수가
2,3,5,7,11,13 이므로
6을 return 한다.

0 이하인 범위가 주어지면 계산하지 않으므로 0을 반환한다.
'''

def prime_num(maxnum):
    '''
    count = 0
    for num in range (2,maxnum+1) 까지
    소수인지 아닌지 판별해서 맞으면 count += 1
        division = 0
        for i in range(2,num)까지
            if num % i ==0
            division = 1 #다른 수로 나누었을 때 나머지가 0이므로 소수가 아님
            break
        if division = 0: # for문을 다 돌아도 0이다. 소수다
            count += 1
    '''
    count = 0
    for num in range(2,maxnum+1):
        division = 0 
        for i in range(2,num):
            if num % i == 0:
                division = 1
                break
        if division == 0 :
            count += 1
    return count

print(prime_num(100))


# prime 값 구하기
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
print(is_real_number(1000)) 
end = datetime.now()
print('걸린 시간 : ',end-start) # 현재 시간 - 함수 시작 시간

'''
