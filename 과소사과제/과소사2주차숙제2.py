# # 주어진 범위 내에서의 배수 갯수 찾는 문제입니다.
# 두 개의 정수 parameter 들을 받으며, 
# 첫번째는 구하는 배수들의 시작값, 두번쨰는 범위입니다.
# 첫번째의 수의 배수가, 0부터 두번째 수까지 몇개가 있는지 찾아서 그 수를 반환합니다.

# 단 주어지는 배수의 시작 수가 음수이거나 0이면 0을 반환합니다.

# 예를 들어서, 2,10 의 값을 받으면, 2의 배수들이 10이하에 5개가 있으므로 5를 반환합니다.
# 5,20의 값을 받으면, 5의 배수들이 20이하에 4개가 있으므로 4를 반환합니다.

from datetime import datetime
def solution(mul, limit):

    count = 0 

    if mul <= 0 :
        return 0
    
    else :
        for i in range(1,limit+1):
            if mul*i <= limit+1:
            # if i % mul == 0:
                count += 1
            else :
                break
    return count
    
start =datetime.now()
print(solution(3,600000))
end = datetime.now()
print('걸린 시간 : ',end-start) # 현재 시간 - 함수 시작 시간



#     answer = 0
#     j = 0
#     mul= int(input())
#     limit = int(input())

#     if mul <= 0 :
#         print(0)
#         return 0

#     else :
#         for i in range in (0,limit+1):
#             if i % mul == 0 :
#                 j += 1
        
#         print(j)
#         return j
#     # mul 은 배수

#     # return answer
# def solution(mul, limit):
#     answer = 0

#     i=0
#     j=0

#     if mul <= 0:
#         return 0

#     else:
#         for i in range (1,limit+1):
#             if i % mul == 0:
#                 j += 1
#         return j

#     return answer