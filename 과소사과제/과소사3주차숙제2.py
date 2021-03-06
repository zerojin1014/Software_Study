# 두 수의 최대 공약 수를 구하는 프로그램을 작성하시오.

# 두 정수가 parameter 로 들어옵니다.
# 이 두 수의 최대공약수를 구하여 반환하시오.
# 단, 두수의 크기에 상관 없는 순서로 parameter 들이 주어집니다.

# 예) 16과 20의 최대공약수는 4이므로 4를 반환합니다.

# def Maxnum(a,b):
#     if b > a :
#         a,b = b,a
    
#     while b !=0 :
#         a,b = b,a%b
#         return(a)

# print(Maxnum(40,24))

def Maxnum(a,b):
    while b != 0 :
        x = a
        a = b
        b = x%b
    
    return(a)

print(Maxnum(24,40))
print(Maxnum(40,24))
''' 8 16 
x = 8 a = 16 b = 8%16 = 8
x = 16 a = 8 b = 16%8 = 0'''


'''
def solution(a,b):
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a

print(solution(12,28))
'''