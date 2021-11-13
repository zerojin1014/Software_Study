#######################  3주차 4 ###############################
message = "철수가 '안녕'이라고 말했습니다."
print(message)

# #문자 앞에 \가 붙으면 문자의 특수한 의미를 잃어버린다.
mesage = "\"Yes,\" I said."
print(mesage)

# # 문자열의 반복
line = '='*100
print(line)

# # %를 사용하여 문자열의 출력 포맷
message = '현재 시간은 % s 입니다.'
time = "12:00pm"
print(message %time)

# ## INDEX

word1 = "Original"
word2 = "Sound"
word3 = "Track"
print(word1[0]+word2[0]+word3[0])

#########################  3주차 5 #############################

# ## 2.5 list의 값 변환
List = [0,1,2,3,4,5]
print(List)
List[2]=22
print(List)

# # *비어있는 리스트는 a = [] 또는 a = list() 로도 만들 수 있다.

a = [1,2,['a','b',['Life','is']]]
print(a[2][2][1])
print(a[0:2])   #리스트 슬라이싱
print(a[:])
print(a[1:])
print(len(a))   #리스트 길이 구하기