

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
# [3, 6, 9, 12]

a = [1,2,3,4]
result = [num ** 2 for num in a if num%2==0 ]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)


##### 함수 #######

def add(a,b) :
    return a+b

print(add(3,5))

def add_many(*args):
    result = 0
    for i in args :
        result += i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10))

def cal_many(choice,*args):
    result = 0 
    if choice == 'add' :
        for i in args :
            result += i
        return result
    elif choice =="mul" :
        result  = 1
        for i in args :
            result *= i
        return result

print(cal_many('add',1,2,3,4,5,6,7,8,9,10))

print(cal_many('mul',1,2,3,4,5,6,7,8,9,10))

#### 키워드 파라미터 kwargs ####
def print_kwarges(**kw):
    return(kw)

A = print_kwarges(a=1, b=2)
print(A)

## 딕셔너리 형태로 출력한다

#