# boolean 자료형

a = True 
b = False

# 리스트나 튜플 딕셔너리가 빈칸이면 False다.

a = [1,2,3,4]
while a :
    print(a.pop())
    print(a)

# 변수란 객체다.
a = [1,2,3]
print(id(a))
b = a
print(id(b))
a.append(4)
a.remove(2)
print(a)
print(b)
print(id(a))
print(id(b))

b = a[:]  ## 주소값이 다르게 복사

from copy import copy
b = copy(a)
print(b)
print(id(a),id(b))
print(b is a)

b = a.copy()
print(id(a),id(b))
print(b is a)

a = 3
b = 5
a,b = b, a
print(a,b)

### if 문
