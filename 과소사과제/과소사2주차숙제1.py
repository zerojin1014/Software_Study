# def solution(statement):
#     answer= 0

#     return answer 
import re

statement = '1234!sqwet-5'
numbers = re.sub(r'[^0-9]', '', statement)
print(numbers)
print(len(numbers))
