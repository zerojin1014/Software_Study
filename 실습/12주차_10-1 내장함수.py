'''
abs(-3) = 3
abs(3+4j) = 5

chr(65) = 'A'   #아스키 코드에 해당하는 문자 반환
ord('A') = 65

# compile(source, filename, mode) 함수

with open('mymodule.py')as f:
    lines = f.read()
    
code_obj = compile(lines, 'mymodule.py', 'exec')
exec(code_obj)

x = complex(4,2)
>>> x
(4+2j)
# 복소수를 표현하는 객체를 생성하는 함수
# real + image * j 형식

# dir 함수
# dir은 객체가 가지고 있는 변수나 함수를 보여 준다.
>>> dir([1,2,3])

# eval() 함수
# eval()은 파이썬의 수식을 문자열로 받아서 실행하고 결과를 반환한다.

>>> eval("1+2");
3

>>> x = 1
>>> y = 1
>>> eval('x'+'y')
2

# exec() 함수 # eval() 의 상위개념
# exec() 함수는 수식뿐만 아니라 모든 파이썬 문장을 받아서 실행한다.

exec("y=2+3")
>>> y
5

>>> statements = """
import math
def area_of_circle(radisu):
    return math.pi*radius*radius
"""
>>> exec(statements)
>>> area_of_circle(5)
78.5398....

# float() 함수
# float() 함수는 문자열을 부동소수점수로 변환하는 기능을 한다.

# max() 함수
# max() 함수는 리스트나 튜플, 문자열에서 가장 큰 항복을 반환한다.

######### 정렬하기 #############
>>> sorted([4,2,3,5,1])
[1,2,3,4,5]

>>> myList = [4,2,3,5,1]
>>> myList.sort()
>>> myList
[1,2,3,4,5]

#### key 매개변수 뭔소린지 모르겠음 ####

>>> students = [
    ('박영진',4.3, 20172289)
    ('김소연',4.5, 20182543)
    ('따식이',3.0, 20204921)
]
            #리스트                #elemet
>>> sorted(students, key = lambda studnet: student[2])
학번 순으로 정렬된다.

##### key 매개변수 클래스 사용 몬소라야 ######


# 오름차순 정렬과 내림차순 정렬
# Reverse 매개 변수가 True 이면 내림차순이 된다.


'''
