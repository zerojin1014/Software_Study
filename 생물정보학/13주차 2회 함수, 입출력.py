# 함수는 결과가 하나다
def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(3,4))
result1 , result2 = add_and_mul(3,4)
print(result1, result2)

##즉 함수는 return문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다.#

def say_nick(nick): 
    if nick == "바보": 
        return 
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')

def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박영진",24)
say_myself("김소연",24,False)

# a = 1
# def vartest():
#     global a
#     a = a +1

# vartest()
# print(a)

a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)


####lambda
#  lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a,b : a+b 
result = add(4,5)
print(result)

import math as m
pita = lambda a,b : m.sqrt(a**2 + b**2)
print(pita(3,4))


################### 입출력 #####################
