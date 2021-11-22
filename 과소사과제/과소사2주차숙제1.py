'''주어진 문자열에서 숫자의 갯수를 세어서 반환하는 문제이다

주어지는 parameter 에는 임의의 문자열이 들어온다.
이 중 숫자의 갯수만을 세어서 반환한다.

예를들어서,
"abc1234!!!" 의 문자열이 주어지면 숫자인 '1234'의 갯수인 4를 반환한다.
'''

def solution(statement):
    count = 0
    List = statement
    for i in ["1","2","3","4","5","6","7","8","9","0"]:
        for j in List:
            if i == j :
                count += 1
    return count

print(solution("12354abc!!!"))


# Message = input("입력하세요 :")
# List = list(Message)
# print (List)
# result = 0

# for i in ["0","1","2","3","4","5","6","7","8","9"]:
#     k = Message.count(i)
#     result += k 

# print(type(Message.count(i)))
# print(result)

# import re

# statement = '1234!sqwet-5'
# numbers = re.sub(r'[^0-9]', '', statement)
# print(numbers)
# print(len(numbers))

# def solution(statement):
#     answer = 0
    
#     import re
#     numbers =re.sub(r'[^0-9]','',statement)
#     return len(numbers)
    
#     return answer
