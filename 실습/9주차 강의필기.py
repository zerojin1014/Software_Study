############## 7-1 튜플 강의################
# 자료구조란 자료들을 저장하는 여러가지 구조들을 자료구조라 한다.

'''
시퀀스에 속하는 자료들은 동일한 연산을 지원한다.
인덱싱, 슬라이싱, 덧셈연산, 곱셈연산

튜플은 변경될 수 없는 리스트 ()
t1 = (1,2,3,4,5)
t1[0] = 100;
>>> 오류가 뜬다

연산은 가능하다.
('Hi',) * 4 = ('Hi','Hi','Hi','Hi')

tuple(seq) : 리스트를 튜플로 변환한다.

student1 = ("철수", 19, "CS")
(name, age, major) = student1
각각의 변수에 assign 된다.

'''
# import math

# def calCircle(r):
#     #반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수 (area, circum)
#     area = math.pi * r * r
#     circum = 2 * math.pi * r
#     return (area, circum)

# radius = float(input("원의 반지름을 입력하시오 : "))
# (a, c) = calCircle(radius)
# print("원의 넓이는" + str(a)+"이고 원의 둘레는 "+str(c)+"이다.")


######### 7-2 세트 강의 #################
# 세트는 우리가 수학에서 배웠던 집합이다.
# 세트는 중복되지 않은 항목들이 모인 것
# 순서가 없다. {} 는 순서가 없다.

# numbers = {2,1,3}
# for x in numbers :
#     print(x, end=' ')

# '''
# numbers = {2,1,3}
# numbers [0]   >>>>>>>>  순서가 없기 때문에 인덱싱이 되지 않는다.
# '''
# # 추가하고 싶을 땐  .add()
# numbers.add(4)
# print(numbers)

# A = {1,2,3,4,5}
# B = {1,2,3}
# B.issubset(A)
# True

# C ={2,5,7}
# D ={1,2,8}
# print(C|D) #C와 D의 합집합
# print(C&D) #C와 D의 교집합
# print(C-B) #C와 D의 차집합

# partyA = set(["Park","Kim","Lee"])
# #{'Lee', 'Kim', 'Park'}
# partyB = set(["Park","Choi"])
# # {'Choi', 'Park'}
# print(partyA,partyB)
# print(partyA.intersection(partyB))

# def process(w):
#     output=''
#     for ch in w:
#         if(ch.isalpha()):
#             output += ch
#     return output.lower()

# words = set()

# fname = input("입력 파일 이름 : ")
# file = open(fname, "r")

# for line in file:
#     lineWords = line.split()
#     for word in lineWords:
#         words.add(process(word))

# print("사용된 단어의 개수 =", len(words))
# print(words)

#### 7-3 딕셔너리 강의 ###############
#딕셔너리는 키와 값의 쌍을 저장할수 있는 객체

# contacts = {"Kim":'0104028100', "Park" :"1231231251", "Jung":"99999234"}
# # contacts[0] >>> 오류 집합에는 순서가 없다.
# print(contacts["Kim"])
# print(contacts.get("Kim"))
# if "Kim" in contacts :
#     print("키가 딕셔너리에 있음")
    
# contacts["Choi"] = "81235212"
# print(contacts)

# print(contacts.pop("Kim")) #Kim의 value를 출력하고 빼버림
# print(contacts)

# scores = { "Korean":90 , "English":60 , "Math":78}
# for x in scores.items():
#     print(x)
# # scores.items() 각각의 key : value 가 하나의 객체가 된다.

# english_dict = dict()

# english_dict['one'] = "하나"
# english_dict['two'] = '둘'

# word=input("단어를 입력해주세요:")
# print(english_dict.get(word, "없음"))
# # dictionary.get(word, "없음") dictionary에 word가 있으면 value 를 없으면 없음

# ###### 단어 카운터 ########
# # IO라서 생략 공부해

# ### 축약어 풀어쓰기###

# table = {"B4"  : "Before",
#          "TX"  : "Thanks",
#          "BBL" : "Be Back Later",
#          "HAND": "Have A Nice Day"}

# message = input("번역할 문장을 입력하시오 : ")
# words = message.split()
# result = ""
# for word in words :
#     if word in table:
#         result += table[word] + " "
#     else :
#         result += word
        
# print(result)


##### 7-4 문자열 More 강의 ###########

#문자열 사전적 앞 뒤 a가 b보다 작다
a = "apple"
b = "orange"

if a < b :
    print(a, "가 앞에 있음")
else:
    print(b, "가 앞에 있음")
    
s = "Legend never die"
print(s.split())

#회문 검사하기 앞으로 읽으나 뒤로 읽으나 동일한 것

def check_pal(s):
    
    #인덱스 위치
    low = 0
    high = len(s) -1
    
    while True :
        if low > high:
            return True;
        
        a = s[low]
        b = s[high]
        
        if a!= b:
            return False
        
        low +=1
        high -= 1
    
    
s = input("문자열을 입력하시오 : ")
s = s.replace(" ", "") #띄어쓰기를 없앤다.

if (check_pal(s) == True) :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")