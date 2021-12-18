'''
[박영진] [오전 10:39] 미니게임 사람 이름으로 궁합 보기.
[박영진] [오전 10:40] 연락처 입력시 하이폰 (-) 삭제 및 다른 특수문자 입력시 오류, 및 예외처리
[박영진] [오전 10:40] 캐시 지우기...?
[박영진] [오후 4:10] 과소사 채점 구동되는 영상(만들 때 구동되는 설명 및 다른프로그램과 비교되는 설명) 제한시간 X 옵션 별로 체크를 할거임 insert delete modify 기능 여러가지로 만들기 5~10분이내 
[박영진] [오후 4:10] input program .. 구동되게 다 모든파일 올리기
설명 많이해주세요 자신만의 강점
[박영진] [오후 4:15] 학생에 대한 기타정보 취미 동아리 지역명 고등학교 명 친구랑만날때 무슨역?
setter getter attribute... str()
오버로딩 메소드 ==  >> 동명이인인 경우 구별할 수 있는 메소드를 만드시오. 연락처를 가지고 구별할 수 있고..


'''

# # 클래스 메소드

class Person : 
    def __init__(self,name,number,e_mail,memo):
        self.name = name
        self.number = number
        self.e_mail = e_mail
        self.memo = memo

    def print_info(self):
        print("Name : " + self.name)
        print("number : " + self.number)
        print("E-mail : " + self.e_mail)
        print("Address : " + self.memo)

#직장 휴대전화 휴대전화 추가 주소 추가 생일 추가 기념일 추가 관계 추가
# 소셜 프로필 추가, 메모

class BestFriends(Person) :
    def __init__(self,name,number,e_mail,memo,address,birthday,anniversary):
        super().__init__ (name,number,e_mail,memo)
        self.__address = address
        self.__birthday = birthday
        self.__anniversary = anniversary

    def getAddress(self):
        return self.__address

    def getBirthday(self):
        return self.__birthday

    def getAnniversary(self):
        return self.__anniversary
    
    def setAddress(self,address):
        self.__address = address
    
    def setBirthday(self, birthday):
        self.__birthday = birthday

    def setAnniversary(self, anniversary):
        self.__anniversary = anniversary

        
#     # 정보 출력
#     def print_info(self) : 
#         print("이름 : ", self.__name)
#         print()

# 기본 메뉴 불러오는 함수

def showMenu() :
    print("---------------------")
    print("1. 연락처 리스트 출력")
    print("2. 연락처 추가")
    print("3. 연락처 삭제")
    print("4. 연락처 변경")
    print("5. 연락처 검색")
    print("9. 저장 및 종료")
    print("---------------------")    
    return int(input("메뉴를 선택하시오 : "))

# 2. 연락처 추가

def addname() : 
    
    name = input("추가하고 싶은 친구 이름을 입력해주세요 : ")
    
    info = []
    while True :    
    
        PhoneNumber = input("전화번호를 입력하세요 : ")
        PhoneNumber = PhoneNumber.replace("-","")
        PhoneNumber = PhoneNumber.replace(" ","")
        
        Isonlynum = 1

        for i in PhoneNumber:
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                Isonlynum = 0

        if Isonlynum == 0 :
            print("연락처 형식이 잘못되었습니다. 다시 입력해주세요.")
            continue

        else :
            info.append(PhoneNumber)
            print(name, PhoneNumber, "가 입력되었습니다.")
        
        option = input("이메일 입력 여부 (O/X) : ")
        if option == 'O' :
            e_mail = input("이메일을 입력해주세요 : ")
            print(name, e_mail, "(이)가 입력되었습니다.")
        else : 
            e_mail = '_'
        info.append(e_mail)
        

        option = input("메모 입력 여부 (O/X) : ")
        if option == 'O' :
            memo = input("메모를 적어주세요. : ")
            print(name, memo, "가 입력되었습니다.") 
        else :
            memo = '_'
        info.append(memo)       

        friends_num[name] = info
        print(name,"님의 연락처가 저장되었습니다.")
        break


    # 번호 대신에 객체를 생성해서 생성한 객체에 ##########################################
    # while Phone_D == True :    
    #     friends_num[name] = PhoneNumber
    #     print(name, PhoneNumber, "가 저장되었습니다.")
    
    # else : 
    #     print("연락처 형식이 잘못되었습니다. 다시 입력해주세요.")

# 3. 연락처 삭제

def delname():
    name = input("삭제하고 싶은 친구 이름을 입력하세요: ")
    if not (name in friends_num) : 
        print("그런 이름은 없습니다.")
    else :
        del friends_num[name]
        print(name, "의 연락처가 삭제되었습니다.")
    
# 4. 연락처 변경

def changeNumber() :
    name = input("변경하고 싶은 친구 이름을 입력하세요 : ")
    if not (name in friends_num) : 
        print("그런 이름은 없습니다.")
    else :
        Newnumber = input("새로운 연락처를 입력해주세요 : ")
        friends_num[name] = Newnumber
        print(name, "의 연락처가 변경되었습니다.")
    
# 5. 연락처 검색

def searchNumber() :
    name = input("검색하고 싶은 친구 이름을 입력해주세요 : ")
    number = friends_num[name]
    print(name,"의 연락처는", number, "입니다. ")
    
# 9. 연락처 저장   

# def saveContact() :
#         outfilename = "friendsList.txt"
#         outfile = open(outfilename, "w", encoding='UTF-8')
        
#         # for name in friends_num : 
#         # print(name,friends_num[name])
#         # outfile.writelines(friends_num+ "\n")
#         str_dic = str(friends_num)
#         outfile.writelines(str_dic+ "\n")
#         print(str_dic)
            
#         outfile.close()

import pickle 
def saveContact() : 
        file = open("friendsList.dat", "wb")
        pickle.dump(friends_num, file)            
        print(friends_num, "\n" , "연락처가 저장되었습니다.")
        file.close()
        
        
# # 00. 연락처 불러오기

def LoadContact():
    file = open("friendsList.dat", "rb")
    global friends_num
    friends_num = pickle.load(file)
    print(friends_num)
    print(type(friends_num))
    file.close()

# def LoadContact():
#     infilename = "friendsList.txt"
#     infile = open(infilename, "r", encoding='UTF-8')
    
#     friends_num = literal_eval()
    
#     # for content in friends_num : 
#     #         print(content)
#     #         infile.writelines(content+ "\n")
            
#     infile.close()

#######################################################################



menu = 0
friends_num = {}

#value 를 객체로
LoadContact()

while menu != 9 :
    
    menu = showMenu()
    
    
    # 연락처 리스트 출력
    if menu == 1 :
        print(friends_num)
    
    # 연락처 추가
    elif menu == 2: 
        name = addname()
    
    # 연락처 삭제
    elif menu == 3:
        name = delname()
    
    # 연락처 변경
    elif menu == 4:
        name = changeNumber()
    
    # 연락처 검색
    elif menu == 5:
        name = searchNumber()
        
    # 연락처 저장
    elif menu == 9 :
        saveContact()
        
# 맨 처음 파일 읽기 

# 리스트를 딕셔너리로