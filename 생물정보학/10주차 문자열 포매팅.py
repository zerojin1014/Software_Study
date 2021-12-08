################### 10주차 내용 ######################

A = "I eat %d apples." %3
print(A)

B = "I eat %s apples." %"five"
print(B)

C = "I eat %f apples." %3.45
print(C)

D = float("3.56")
print(D)
print(type(D))

number = 3

E = "I eat %d apples." %number
print(E)

day = "three"
F = "I ate %d apples. so I was sick for %s days." %(number, day)
print(F)

G = "rate is %s%%"%3.24
print(G)

'''
1. 정렬과 공백

>>> "%10s" % "hi"
'        hi'
앞의 예문에서 %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.

그렇다면 반대쪽인 왼쪽 정렬은 %-10s가 될 것이다. 확인해 보자.

>>> "%-10sjane." % 'hi'
'hi        jane.'
hi를 왼쪽으로 정렬하고 나머지는 공백으로 채웠음을 볼 수 있다.

'''

H = "%10s" %"hi"        #전체 10자리 중 오른쪽 정렬쓰기
print(H)

H1 = "%10s" %"hihi"
print(H1)

H2 = "%-10sjane." %"hi"
print(H2)
#>>> |hi        jane.|
#>>> 01234567891

'''
2. 소수점 표현하기

>>> "%0.4f" % 3.42134234
'3.4213'
3.42134234를 소수점 네 번째 자리까지만 나타내고 싶은 경우에는 위와 같이 사용한다. 즉 여기서 '.'의 의미는 소수점 포인트를 말하고 그 뒤의 숫자 4는 소수점 뒤에 나올 숫자의 개수를 말한다. 다음 예를 살펴보자.

>>> "%10.4f" % 3.42134234
'    3.4213'
위 예는 숫자 3.42134234를 소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예를 보여 준다.
'''

H3 = "%10.4f" %3.45125125
print(H3)
#>>> |    3.4513|
#>>> |0123456789

H31 = "%0.4f" %3.45125125
print(H31)
#>>> |3.4513
#>>> |0123456
H32 = "%08.4f" %3.45125125
print(H32)
#>>> |003.4513
#>>> |01234567 >> 전체공간 8자리에서 소수점 4자리까지 나머지는 0
H33 = "%09.4f" %3.45125125
print(H33)
#>>> |0003.4513
#>>> |012345678 >>전체공간 9자리에서 소수점 4자리까지 나머지는 0
H34 = "%-08.6f" %3.4512
print(H34)
#>>> |3.451200 
#>>> |01234567 >> 전체공간 8자리에서 왼쪽정렬 

G = "I eat {0} apples.".format(5)
print(G)

G1 = "I eat {0} apples.".format("five")
print(G1)

G2 = "I eat {0} apples.".format(number)
print(G2)

number, day = 10, "five"

G3 = "I ate {0} apples. so I was sick for {1} days.".format(number,day)
print(G3)

G3 = "I ate {1} apples. so I was sick for {0} days.".format(number,day)
print(G3)

### {0}, {1}은 (튜플) 의 인덱스다 
G3 = "I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)
print(G3)

G4 = "{0:<10}".format("hi")
print(G4)

G4 = "{0:>10}".format("hi")
print(G4)

G4 = "{0:^10}".format("hi")
print(G4)

G4 = "{0:=^20}".format("hi")
print(G4)

### format의 인덱스 0을 불러오는데 : 조건이 있습니다.
### =를 채우고 ^ 가운데 정렬하고 10자리 빈칸이 있습니다.

G4 = "{0:!^20}".format("hi")
print(G4)
# >>> !!!!!!!!!hi!!!!!!!!!
G4 = "{0:=>20}".format("hi")
print(G4)
# >>> ==================hi
G4 = "{0:@<20}".format("hi")
print(G4)
# >>> hi@@@@@@@@@@@@@@@@@@

y = 3.42145
G5 = "{0:10.4f}".format(y)
print(G5)

G5 = "{{and}}".format()
print(G5)

###### f 문자열 포매팅 ###########
name = "홍길동"
age = 30
A = f"나의 이름은 {name} 입니다. 나이는 {age} 입니다."
print(A)

A = f"나는 내년이면 {age+1} 살이 된다"
print(A)

d = {"name":"박영진", "age":24}
print (f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.')

print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=<10}')

y = 3.123456
print(f'{y:0.4f}')
print(f'{y:<20.4f}')
print(f'{y:-10.4f}')