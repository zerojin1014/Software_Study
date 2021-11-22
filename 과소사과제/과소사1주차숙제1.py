# 문자열의 중앙에 있는 문자를 출력한다.
# weekday면 중앙의 문자열은 k가 된다. 하지만 만약 문자열이 짝수개의 문자를 가지고 있다면
# 중앙의 2개의 글자를 출력한다. 예를 들어서 string 문자열에서는 ri를 반환한다.

munja = input(":")
a = len(munja)

if a% 2 == 1: #012
    print(munja[a//2])

elif a % 2 == 0 : #0123
    print(munja[(a//2)-1], end='')
    print(munja[a//2])
    

# string = input(":")
   
# if len(string) %  2 == 1 :  #01234
#    print(string[(len(string)//2)])

# elif len(string) % 2 == 0 : #0123
#     print(string[(len(string)//2)], end=" ")
#     print(string[((len(string)//2)-1)])

# def solution(str):
#     answer = ''
#     if len(str)%2==1:
#         return str[len(str)//2]
#     else:
#         return str[(len(str)//2-1): len(str)//2+1]
#     return answer

# 접근 목표 string이 홀수일때 인덱스 > weekday = 0123456 string의 길이/2 의 문자를 추출한다. 
# string이 짝수일 때 string = 012345 string/2

#문자열에서 원하는 부분을 추출(슬라이싱) 하기 위해서는 인덱스의 숫자를 적어준다.

# 다음 예제를 보면, 콜론( : ) 앞과 뒤에 숫자를 써준다.
# 앞에 써주는 숫자는, 시작 인덱스를 나타낸다.
# 뒤에 써주는 숫자는,  그 숫자 - 1 의 인덱스까지 추출 해 오겠다는 뜻이다.

# 중요!
# 콜론 왼쪽 숫자 = 우리가 추출하기 원하는 시작 인덱스 
# 콜론 오른쪽에 써주는 숫자 = 우리가 추출하기 원하는 끝 인덱스 + 1 

# s="qwer"

# def solution(s):
#     answer = s[len(s)-1//2:len(s)//2+1]
#     return answer
   
   
#     if len(s) % 2 == 1:
#         return s[len(s)//2]
#     else:
#         return s[(len(s)//2-1) : len(s)//2+1]

# print(s[2:3])

# def solution(str):
#     answer = ''
#     if len(str)%2==1:
#         return str[len(str)//2]
#     else:
#         return str[(len(str)//2-1): len(str)//2+1]
#     return answer