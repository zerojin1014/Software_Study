# 튜플은 변경불가!

t1 = (1,2,3,4)
print (t1[0:2])

t1 += (6,5)
print(t1)

# 딕셔너리 
# 키에는 변하지 않는 값을 사용하고 Value에는 변하는값과 변하지 않는거 모두 사용 가능
A = {'Key1':'Value1', 'Key2':'Value2'}
print(A)
print(A['Key1'])

A[1] = 'b' #인덱스가 아님
print(A)
A['name'] = 'yeong'
print(A)
del A['name']
print(A)

# 중복되는 Key가 있으면 하나를 제외한 나머지 모든 것들이 제외된다.
# 동일한 Key가 존재하면 어떤 Value 몰라
# Key에 리스트는 못씀 but 튜플은 쓸 수 있다.

Keys = A.keys()
# >>> dict_keys(['Key1', 'Key2', 1])  >>> 바꿀 수 없다
Keys = list(A.keys())
# >>> ['Key1', 'Key2', 1] >>>>>> 그래서 list 넣어서 새로 한다.
print(Keys)

for k in A.keys() :
    print(k)

# Key Value 쌍 얻기
print(A.items())

# Key : Value 쌍 모두 지우기(clear)
A.clear()
print(A)


A = {'Key1':'Value1', 'Key2':'Value2'}
# A['name'] , A.get('name') 차이점
print(A.get('name'))
# >>> None (오류 안뜸)
# print(A['name'])
# >>> 오류 뜸
print(A.get('name','Yeongjin'))
# 만약에 name이라는 key가 없으면 yeongjin을 반환해라

#### 딕셔너리 안에 있는지  조사하기

if ('name' in A) is False:
    print("없어용")



######### 집합형 자료형 #######
s1 = set({1,2,3})
print(s1)

B = set("apple")
print(B)
# >>> {'e', 'a', 'l', 'p'}
# 중복을 허용하지 않음
# 순서가 없다. >>> 인덱싱 불가

C = list(B)
C.sort()
print(C)
print(C[0])

D = set(C)
print(D)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1 & s2)
print(s1 - s2)
print(s1 | s2) # +가 아니라 | 다.

s1.add(7)
print(s1)
s1.update({9,10,8})
print(s1)
s1.remove(2)
print(s1)