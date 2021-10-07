# 1 = ture 0 = false

# 논리 연산자
# x and y : x와 y가 모두 참이면 참 그렇지 않으면 거짓
# x or y : x 나 y 중에서 하나만 참이면 참 모두 거짓이면 거짓
# not x : x가 참이면 거짓, x가 거짓이면 참

# 아이디를 입력받아서 등록된 아이디인지 검사하는 프로그램
# 등록된 아이디를 리스트(list)에 저장하도록 한다. 아이디가 일치하면 패스워드 물어본다.

IdList = ['koalapyj','zerojin1014','20172289','koalapyj1']
Id = input("아이디를 입력하시오: ")

if Id in IdList:
    passWord= input("패스워드를 입력하시오: ")
    if passWord == "123456":
        print("환영합니다!")
    else :
        print("잘못된 패스워드입니다.")

else :
    print("등록되지 않은 회원입니다.")


