############## 파일 읽고 쓰기 ############
import os
print(os.getcwd())

f = open("C:/Users/koala/OneDrive/바탕 화면/파이썬/과소사/Software_Study/생물정보학/새파일.txt",'r')
# 절대경로
# C:/Users/koala/OneDrive/바탕 화면/파이썬/과소사/Software_Study/생물정보학/
# 상대경로
# ../
# a = f.readlines()
# a = f.readline()
# b = f.readline()

# while 1 :
#     line = f.readline()
#     if not line : break
#     # print(line, end=(""))
#     print(line.strip("\n"))

a = f.read() # 파일 전체를 str으로 
print(a)
print(type(a))
f.close()

f = open("C:/Users/koala/OneDrive/바탕 화면/파이썬/과소사/Software_Study/생물정보학/temp.txt",'w')
f.write("123456789\n")
f.write("123455")
f.close()

# 현재 경로 : 오픈폴더가 SOFTWARE_STUDY이므로
# C:\Users\koala\OneDrive\바탕 화면\파이썬\과소사\Software_Study
m = open("생물정보학/temp.txt", 'w')
m.write("가나다라마바사")
m.close()

b = open("C:/Users/koala/OneDrive/바탕 화면/파이썬/과소사/Software_Study/생물정보학/temp.txt",'r')
c = b.readlines()
print(c)
# f = open >>>> 파일을 연 상태의 객체

######################################################
''' 파일을 w모드로 열면 안에 내용들이 싹 다 사라진다
 a모드로 열면 추가 가능 '''
 ######################################################