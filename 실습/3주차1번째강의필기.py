#########################  3주차 1 ############################# 

# 변수의 값 교환

x = 20
y = 30
tmp = x
x = y
y = tmp

print(x,y)

#########################  3주차 2 #############################  

# 나눗셈 // 몫   나눗셈 / 그 값  나머지 % 지수 **

a = 1000 ; r= 0.05 ; n = 10 
print(a*(1+r)**n)

sec = 1000
minute = 1000//60
remainder = 1000%60
print(minute,remainder)

x = 2
y = 3 * x**2 + 7*x + 9
print(y)

#########################  3주차 3 #############################  

value= abs(-3)  # 절댓값
print(value)

print(round(1.231)) # 반올림

print(max(10,20)) # 둘 중 큰 값
print(min(12,14,15,156,11,55,3)) #둘중 작은 값

import math as m
from math import * # math에 있는 모든 함수를 쓴다
from typing import SupportsRound

print(sqrt(4.0))  # 루트값

#  거리 = 속도 * 시간

print(type(sec))
print(type(value))

# 구의 부피 계산하기 
r = int(input(":"))
Volume = 4/3*(m.pi)*r**3
print(round(Volume,3))

