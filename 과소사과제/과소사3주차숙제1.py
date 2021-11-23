# 주어지는 수가 소수(prime) 인지를 판별하는 프로그램을 작성하시오
# 소수는 1과 그 수 자신이외의 자연수로는 나눌 수 없는 1보다 큰 자연수 입니다.
# 예 1) 5는 소수이므로 참 값을 반환합니다.
# 예 2) 8은 소수가 아니므로 거짓 값을 반환합니다.

# def prime_number (num):
#     for i in range(1,num):
#         if num % i == 0 :
#             return False
#     return True
    
def solution(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True



'''
def solution(num):

    for i in range(2, num):
        if num % i == 0:
            return False 

    return True
'''