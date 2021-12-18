# 기본 메뉴 불러오는 함수

def showMenu() :
    print("---------------------")
    print("1. 연락처 리스트 출력")
    print("2. 연락처 추가")
    print("3. 연락처 삭제")
    print("4. 연락처 변경")
    print("5. 연락처 검색")
    print("9. 종료")
    
    return int(input("메뉴를 선택하시오 : "))

# 클래스 메소드

class Person :
    def __init__(self,name,number):
        self.__name = name
        self.__number = number

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def setName(self,name):
        self.__name = name
    
    def setNumber(self, number):
        self.__number = number



# 2. 연락처 추가

def addname() : 
    name = input("추가하고 싶은 친구 이름을 입력해주세용 : ")
    PhoneNumber = input("전화번호를 입력하세요 : ")
    
    # 번호 대신에 객체를 생성해서 생성한 객체에 ##########################################
    friends_num[name] = PhoneNumber
    print(name, PhoneNumber, "가 저장되었습니다.")

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