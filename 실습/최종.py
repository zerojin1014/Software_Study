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
# 일반사람
class Person : 
    def __init__(self,name,info):
        self.name = name
        self.info = info
    
    def __str__(self) :
        return '이름 : {}, 정보 : {}'.format(self.name, self.info)

    def print_info(self):
        print("Name   : " + self.name)
        print("number : " + self.info[0])
        print("E-mail : " + self.info[1])
        print("Memo   : " + self.info[2]) 
        print("")

# 친한 친구로 등록한 사람
class BestFriends(Person) :
    def __init__(self,name,info,bestinfo):
        super().__init__ (name,info)
        self.__bestinfo = bestinfo

    def print_info(self):
        print("Name         : " + self.name)
        print("number       : " + self.info[0])
        print("E-mail       : " + self.info[1])
        print("Memo         : " + self.info[2]) 
        print("Address      : " + self.__bestinfo[0])
        print("Birthday     : " + self.__bestinfo[1])
        print("Anniversary  : " + self.__bestinfo[2])


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
def add_Contact() : 
    
    # 이름 입력
    name = input("추가하고 싶은 친구 이름을 입력해주세요 : ")

    # 정보 입력
    info = []
    while True :    

        # 전화번호 입력
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
        
        # 이메일 입력
        option = input("이메일 입력 여부 (O/X) : ")
        if option == 'O' :
            e_mail = input("이메일을 입력해주세요 : ")
            print(name, e_mail, "(이)가 입력되었습니다.")
        else : 
            e_mail = '_'
        info.append(e_mail)
        
        # 메모 입력
        option = input("메모 입력 여부 (O/X) : ")
        if option == 'O' :
            memo = input("메모를 적어주세요. : ")
            print(name, memo, "가 입력되었습니다.") 
        else :
            memo = '_'
        info.append(memo)       
        print(name,"님의 연락처가 저장되었습니다.")

        contact = Person(name,info)
        return contact

# 3. 연락처 삭제
def del_Contact(contact_list, name):
    for i, contact in enumerate(contact_list) :     
        if contact.name != name : 
            print("그런 이름은 없습니다.")
        else :
            del contact_list[i]
            print(name, "의 연락처가 삭제되었습니다.")
    
# # 4. 연락처 변경
# def change_Contact(contact_list, name) :
#     for i, contact in enumerate(contact_list) :     
#         if contact.name != name : 
#             print("그런 이름은 없습니다.")
#         else :
#             del contact_list[i]
#             print(name, "의 연락처가 삭제되었습니다.")
    
#     if not (name in friends_num) : 
#         print("그런 이름은 없습니다.")
#     else :
#         Newnumber = input("새로운 연락처를 입력해주세요 : ")
#         friends_num[name] = Newnumber
#         print(name, "의 연락처가 변경되었습니다.")
    
# # 5. 연락처 검색

# def searchNumber() :
#     name = input("검색하고 싶은 친구 이름을 입력해주세요 : ")
#     number = friends_num[name]
#     print(name,"의 연락처는", number, "입니다. ")
    
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
def saveContact(contact_list) : 
        file = open("friendsList.dat", "wb")
        pickle.dump(contact_list, file)            
        print("연락처가 저장되었습니다.")
        file.close()
        
        
# # 00. 연락처 불러오기

def LoadContact(contact_list):
    file = open("friendsList.dat", "rb")
    contact_list = pickle.load(file)
    file.close()


# 연락처 출력하기
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# def LoadContact():
#     infilename = "friendsList.txt"
#     infile = open(infilename, "r", encoding='UTF-8')
    
#     friends_num = literal_eval()
    
#     # for content in friends_num : 
#     #         print(content)
#     #         infile.writelines(content+ "\n")
            
#     infile.close()

#######################################################################
def run ():
    menu = 0
    contact_list =[]

    try : 
        LoadContact(contact_list)

    except EOFError :
        print("파일에 내용이 없습니다.")

    while menu != 9 :
        
        menu = showMenu()
        
        
        # 연락처 리스트 출력
        if menu == 1 :
            print_contact(contact_list)
        
        # 연락처 추가
        elif menu == 2: 
            contact = add_Contact()
            contact_list.append(contact)
        
        # 연락처 삭제
        elif menu == 3:
            name = input("연락처를 지우고 싶은 사람을 입력해주세요 : ")
            del_Contact(contact_list, name)
        
        # 연락처 변경
        elif menu == 4:    
            name = input("변경하고 싶은 사람 이름을 입력하세요 : ")
            change_Contact(contact_list, name)
        
        # 연락처 검색
        elif menu == 5:
            name = searchNumber()
            
        # 연락처 저장
        elif menu == 9 :
            saveContact(contact_list)
            
    # 맨 처음 파일 읽기 

    # 리스트를 딕셔너리로

run()