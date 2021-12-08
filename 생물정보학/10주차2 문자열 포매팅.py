### 문자열 내장 함수 ###

a = "hobby is the best choice"
####|012345678901234567890123|

print(a.count('b'))
# >>> 3

print(a.find('b'))
# >>> 2 #제일 처음 b를 보여준다.

print(a.find('z'))
# >>> -1 # -1은 없을 때 return 한다.

print(a.index('b'))
# >>> 2 
# print(a.index('z'))
# >>> ValueError # 없으면 에러를 발생시킨다.

print(",".join('abcd'))
# 사이 사이에 ,을 집어넣어라
# >>> a,b,c,d
A = ",".join(['a','b','c','d'])
print(A)
# >>> a,b,c,d

A = (a.upper())
print(A)

A= A.lower()
print(A)

##### 10칸 불러오고 공백 없애기 두점 사이의 거리 ########## 중요
a = "    hi    "
print(a.lstrip()) #왼쪽공백 없애기
print(a.rstrip()) #오른쪽공백 없애기
print(a.strip()) #양쪽공백 없애기 ###########중요######

#######a 문자열 바꾸기########
a = "Life is too short"
print(a.replace("Life","Your Leg"))
print(a.replace(" ",""))

###### 문자열 나누기 #######
print(a.split())

a = "a:b:c:d:e"
print(a.split(':'))


##### 리스트 자료형 ########
a = [[1,2],[3,4]]
print(a[0][1])

#determinant = ad - bc
c = a[0][0]*a[1][1] - a[0][1]*a[1][0]
print(c)

A = [1,2,3] 
print(A)

B = "%s"%A[2] + "hi"
print(B)
B = str(A[2]) + "hi"
print(B)

#### tuple은 바꿀 수 없다 ##

a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,65,6]
del a[4:]
print(a)

a = [1,2,3,4]
a.append(5)
print(a)
a.append(3)
print(a)
a.sort()
print(a)

a = ["m","c","a","b"]

print(a)
'''
리스트에 요소 삽입(insert)
insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다. 파이썬에서는 숫자를 0부터 센다는 것을 반드시 기억하자.

>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]
위 예는 0번째 자리, 즉 첫 번째 요소(a[0]) 위치에 값 4를 삽입하라는 뜻이다.

>>> a.insert(3, 5)
>>> a
[4, 1, 2, 5, 3]
위 예는 리스트 a의 a[3], 즉 네 번째 요소 위치에 값 5를 삽입하라는 뜻이다.

리스트 요소 제거(remove)
remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.

>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]
a가 3이라는 값을 2개 가지고 있을 경우 첫 번째 3만 제거되는 것을 알 수 있다.

>>> a.remove(3)
>>> a
[1, 2, 1, 2]

'''

