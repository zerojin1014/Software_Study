# 최대공약수 구하는 문제

# 유클리드 알고리즘
# 최대공약수 구하기 !!!! 
# 40=(2*2*2*5) 와 24=(2*2*2*3) 의 최대공약수 = 8(2*2*2)
# 정수 a 와 b 의 최대공약수 (a>= b>0)를 G(a,b)라고 하면

# if b == 0 면 종료 , a가 최대 공약수
# a=b ,b=a%b
# 1,2 반복

# a= int(input("A :")) ; b= int(input("B:"))
# while (b != 0) :
#     # x=a
#     # a=b
#     # b=x%b
#     a,b=b,a%b       #이런식으로 간단하게 만들 수도 있다.
# print("GCD is %d" %a)

def solution(a,b):

    while b != 0:
        x = a
        a = b
        b = x%b
    return a

print(solution(24,40))