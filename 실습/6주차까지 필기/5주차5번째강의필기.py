######################  5주차 5  ################################ 

# 중첩 루프 
# 중첩 for 문을 이용하여 *기호를 사각형 모양으로 출력하는 프로그램

from typing import Counter


for y in range(5):
    for x in range(10):
        print("*",end="")
    print("")

# 직각삼각형 찾기
# 각 변의 길이가 100보다 작은 삼각형 중에서
# 피타고라스의 정리가 성립하는 직각삼각형은 몇 개나 있을까?
# n = 0
# for a in range(1,101,1):
#     for b in range(1,101,1):
#         for c in range(1,101,1):
#             if (a**2 + b**2) == c**2:
#                 n += 1
#                 print(a,b,c); print(n)

# 문자열도 시퀀스의 일종

fruit = "apple"
for letter in fruit:
    print(letter, end=" ")

# 모음을 삭제하는 문자열 처리 예제 !!중요할거같음..

s =input("문자열을 입력하세요 : ")
vowels = "aeiouAEIOU"
result = ""
count = 0
for i in s :
    if i not in vowels:
        result += i
    else : 
        count += 1
print(result, count)

# s = input("문자열을 입력하세요: ")
# vowels = "aeiouAEIOU"
# result = ""
# for letter in s:
#     if letter not in vowels:
#         result += letter
# print(result)

# 자음과 모음 개수 구하는 예제

# s = input("문자열을 입력하세요: ")
# word = s.lower() #문자열에 lower() 는 소문자로
# vowels = 0 
# consonants = 0

# if len(s) > 0 and s.isalpha(): #isalpha 는 s.가 알파벳이면
#     for letter in word:
#         if letter in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1

# print("모음의 개수 :",vowels)
# print("자음의 개수 :",consonants)

# 문자열의 문자 숫자 스페이스 개수 출력하기
##### 


# s = input("문자를 입력하세요: ")

# alphas = 0
# digits = 0
# space = 0

# for i in s:
#     if i.isalpha():     ###isalpha() 할때 () 꼭 하기
#         alphas += 1
#     elif i.isdigit():
#         digits += 1
#     elif i.isspace():
#         space += 1

# print(alphas, digits, space)


# 전화번호 처리

# 전화번호를 입력하세요 
num = input("전화번호를 입력하세요 : ")
result = ""

for i in num:
    if i != "-":
        result += i
print(result)


# for i in num:
#     if i != "-":
#         result += i
# print(result)