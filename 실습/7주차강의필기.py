# 6-1 리스트 개념 강의

# scores = []
# for i in range(10):
#     scores.append(int(input("성적을 입력하시오 : ")))
# print(scores)

# for i in range(0):

# len() 길이계산
# 2개의 시퀀스 연결 +
######### * 반복 [Welcom!]* 3 = [Welcom!,Welcom!,Welcom!]
# in 소속
# not in 소속하지 않음
# [] 인덱스
# min() 시퀀스에서 가장 작은 요소
# for 루프 : for x in [1,2,3] : print(x)  

# a = [1,3,5,6,2,4]
# b=sorted(a)
# a.sort()

# print(a)
# print(b)

# list1 = [3,4,5]
# list2 = [x**2 for x in list1]
# print(list2)

# new_list = []
# new_list = [(x,y,z) for x in range(1,30) for y in range(1,30) for z in range(1,30) if x**2 + y**2 == z**2]
# print(new_list)

# 2차원 리스트
'''
from typing import List


s = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(s)
rows = (len(s))
cols = (len(s[0]))

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")
    print()
rows = 3
cols = 5
'''
# s = []
# for row in range(rows):
#     s +=[[0]*cols]

# print("s=",s) 

rows = 6
cols = 6
table = []

# 2차원 리스트를 생성한다.
for row in range(rows):
        table += [[0]*cols]
# print(table)    
# 2차원 리스트에 각각의 요소들을 더한다.
for row in range(rows):
    for col in range(cols):
        table[row][col] = (row+1+col+1)
print(table)
