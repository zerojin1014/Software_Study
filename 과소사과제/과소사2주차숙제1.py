# def solution(statement):
#     answer= 0

#     return answer 


Message = input("입력하세요 :")
List = list(Message)
print (List)
result = 0

for i in ["0","1","2","3","4","5","6","7","8","9"]:
    k = Message.count(i)
    result += k 

print(type(Message.count(i)))
print(result)

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
