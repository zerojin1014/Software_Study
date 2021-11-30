# 범위 내의 피보나치 수열의 마지막 값을 구하는 프로그램을 작성하세요.
# 주어진 parameter 값 내에서 피보나치 수열을 생성할 때 가장 마지막 수를 return 하시오.

# 예) 1000의 값을 주면, 피보나치 수열을
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# 이므로, 마지막 값인 987을 반환한다.

def pibo(lastnum):

    '''
    피보나치 수열 진행 
    a b 
    쭉쭉쭉쭉 하다가
    if 수열의 b 값이 > lastnum 면 a값 리턴'''

    a,b = 0,1
    while b >= lastnum:
        a,b = b,a+b
    return a

print(pibo(1000))


# def solution(n):
#     a = 0 
#     b = 1
#     c = a+b

#     while c <= n :
#         a = b
#         b = c
#         c = a + b

#     return(b)

# def solution(n):
#     result = []
#     a, b = 0, 1
#     while a <= n:
#         result.append(a)
#         a, b = b, a+b
#     return result[-1]

# for i in range (0,6000):
#     print(solution(i))

def solution(n):
    a = 0 
    b = 1
    c = a+b

    if n <= 0:
        return(0)
    else:

        while c <= n :
            a = b
            b = c
            c = a + b

        return(b)
print(solution(1000))