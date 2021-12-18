# 일반사람
class Person : 
    def __init__(self,name,number,E_mail='',memo=''):
        self.name = name
        self.number = number
        self.E_mail = E_mail
        self.memo = memo
    
    def __str__(self):
        return '(%d, %d, %d, %d)' %(self.name,self.number,self.E_mail,self.memo)
        
    def __eq__(self, other):
        return (self.name == other.name) and (self.number == other.number)
    
    def setName(self,name):
        self.name = name
    def setNumber(self,number):
        self.number = number
    def setEmail(self,E_mail):
        self.E_mail=E_mail
    def setMemo(self,memo):
        self.memo = memo
        
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def getEmail(self):
        return self.E_mail
    def getMemo(self):
        return self.memo
    
    def print_info(self):
        print("Name   : " , self.name)
        print("number : " , self.number)
        print("E-mail : " , self.E_mail)
        print("Memo   : " , self.memo) 
        print("")

# 친한 친구로 등록한 사람
class BestFriends(Person) :
    def __init__(self,name,number,E_mail,memo,address='',birthday='',anniversary=''):
        super().__init__ (name,number,E_mail,memo)
        self.__address = address
        self.__birthday = birthday
        self.__anniversary = anniversary
        
    def __str__(self):
        return '(%d, %d, %d, %d, %d, %d, %d)' %(self.name,self.number,self.E_mail,self.memo,self.__address,self.__birthday,self.__anniversary)    
    
    def setAddress(self,address):
        self.__address = address
    def setBirthday(self, birthday):
        self.__birthday = birthday
    def setAnniversary(self, anniversary):
        self.__anniversary = anniversary
        
    def getAddress(self):
        return self.__address
    def getBirthday(self):
        return self.__birthday
    def getAnniversary(self):
        return self.__anniversary
        
    def print_info(self):
        print("Name         : " + self.name)
        print("number       : " + self.number)
        print("E-mail       : " + self.E_mail)
        print("Memo         : " + self.memo) 
        print("Address      : " + self.__address)
        print("Birthday     : " + self.__birthday)
        print("Anniversary  : " + self.__anniversary)


# 기본 메뉴 불러오는 함수
def showMenu() :
    print("--------------------------------")
    print("총",len(contact_list),"개 의 연락처가 있습니다.")
    print("1. 연락처 리스트 출력")
    print("2. 연락처 추가")
    print("3. 연락처 삭제")
    print("4. 연락처 변경")
    print("5. 연락처 검색")
    print("9. 저장 및 종료")
    print("-------------------------------")    
    return int(input("메뉴를 선택하시오 : "))

def BestshowMenu(): 
    print("==============================================")
    print("=============== Secret Friends ===============")
    print("==============================================")
    print("===== 총",len(bestcontact_list),"개 의 비밀 연락처가 있습니다. =====")
    print("=======  1. 비밀 연락처 리스트 출력  ==========")
    print("=======    2. 비밀친구 추가    ================")
    print("=======    3. 비밀친구 삭제    ================")
    print("=======    4. 비밀친구 변경    ================")
    print("======     5. 비밀친구 검색    ================")
    print("======= 9. 원래 메뉴로 돌아가기 ===============")
    print("==============================================")    
    return int(input("메뉴를 선택하시오 : "))

# 1. 연락처 출력하기
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 2. 연락처 추가
def add_Contact() : 
    
    # 이름 입력
    name = input("추가하고 싶은 친구 이름을 입력해주세요 : ")

    # 정보 입력
    distinction = 1
    while distinction != 0  :    

        # 전화번호 입력
        number = input("전화번호를 입력하세요 : ")
        number = number.replace("-","")
        number = number.replace(" ","")
        
        Isonlynum = 1

        for i in number:
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                Isonlynum = 0

        if Isonlynum == 0 :
            print("연락처 형식이 잘못되었습니다. 다시 입력해주세요.")
            continue

        else :
            print(name, number, "가 입력되었습니다.")
        
        
        A = number 
        for i, contact in enumerate(contact_list) :     
            B = contact.getNumber()
            if A == B :
                distinction = 0
                print("중복된 번호 입니다.")
                
        if distinction == 0 :
            break
        
        # 이메일 입력
        E_mail = input("이메일을 입력해주세요 : ")
    
        # 메모 입력
        memo = input("메모를 적어주세요. : ")
  
        print(name,"님의 연락처가 저장되었습니다.")
        
        contact = Person(name,number,E_mail,memo)
        return contact

# 3. 연락처 삭제
def del_Contact(contact_list, name):
    for i, contact in enumerate(contact_list) :     
        if contact.name == name : 
            del contact_list[i]
            print(name, "의 연락처가 삭제되었습니다.")
            break
    else : 
        print("그런 이름은 없습니다.")
            
    
# # 4. 연락처 변경
def change_Contact(contact_list, name) :
    for i, contact in enumerate(contact_list) :     
        if contact.name == name :  
            name = input("새로운 이름을 입력해주세요 : ") 
            contact.setName(name)
            
            number = input("전화번호를 입력하세요  : ")
            number = number.replace("-","")
            number = number.replace(" ","")
            contact.setNumber(number)
                 
            E_mail = input("이메일을 입력해주세요 : ")
            contact.setEmail(E_mail)         
               
            memo = input("메모를 적어주세요. : ")
            contact.setMemo(memo)
            print("저장되었습니다.") 
            break
    else : 
        print("그런 이름은 없습니다.")
    
# 5. 연락처 검색
def search_Number(contact_list, name) :
    for i, contact in enumerate(contact_list) :     
        if contact.name == name :  
            contact.print_info()
            break
    else : 
        print("그런 이름은 없습니다.")
    
# 6. 친한 친구 등록하기
def add_Bestfriends(contact_list, name) :
    for i, contact in enumerate(contact_list) :     
        if contact.name == name :  
            address = input("주소를 입력해주세요 : ") 
            birthday = input("생일을 입력하세요  : ")  
            anniversary = input("기념일을 입력해주세요 : ")
            number = contact.getNumber()
            E_mail = contact.getEmail()
            memo = contact.getMemo()
            
            Bestcontact = BestFriends(name,number,E_mail,memo,address,birthday,anniversary)
            return Bestcontact
    else : 
        print("그런 이름은 없습니다.")
        
def del_Bestfriends(bestcontact_list, name):
    for i, contact in enumerate(bestcontact_list) :     
        if contact.name == name : 
            del bestcontact_list[i]
            print(name, "(이)가 비밀 친구에서 해제되었습니다.")
            break
    else : 
        print("그런 이름은 없습니다.")
        
def change_Bestfriends(bestcontact_list, name) :
    for i, contact in enumerate(bestcontact_list) :     
        if contact.name == name :  
            name = input("새로운 이름을 입력해주세요 : ") 
            contact.setName(name)
            
            address = input("새로운 주소를 입력해주세요 : ") 
            contact.setAddress(address)
            
            birthday = input("새로운 생일을 입력하세요  : ")
            contact.setNumber(birthday)
                 
            anniversary = input("새로운 기념일을 입력해주세요 : ")
            contact.setEmail(anniversary)         
               
            print("저장되었습니다.") 
            break
    else : 
        print("그런 이름은 없습니다.")
        
def search_Bestfriends(bestcontact_list, name) :
    for i, contact in enumerate(bestcontact_list) :     
        if contact.name == name :  
            contact.print_info()
            break
    else : 
        print("그런 이름은 없습니다.")    


# 연락처 저장하기

import pickle 
def saveContact(contact_list) : 
    file = open("friendsList.dat", "wb")
    pickle.dump(contact_list, file)  
    pickle.dump(bestcontact_list, file)          
    print("연락처가 저장되었습니다.")
    file.close()
        
# 연락처 불러오기
def LoadContact():
    file = open("friendsList.dat", "rb")
    global contact_list
    contact_list = pickle.load(file)
    global bestcontact_list
    bestcontact_list = pickle.load(file)
    file.close()

#######################################################################
contact_list = []
bestcontact_list = []

def run ():
    menu = 0
    
    
    try : 
        LoadContact()
        
    except EOFError :
        print("파일에 내용이 없습니다.")

    while menu != 9 :
       
        secretmenu = 0
        menu = showMenu()
        
        # 연락처 리스트 출력
        if menu == 1 :
            print_contact(contact_list)
        
        # 연락처 추가
        elif menu == 2: 
            contact = add_Contact()
            try : ...
            except : AttributeError
            finally : contact_list.append(contact)
        
        # 연락처 삭제
        elif menu == 3:
            name = input("연락처를 지우고 싶은 사람을 입력해주세요 : ")
            del_Contact(contact_list, name)
        
        # 연락처 변경
        elif menu == 4:    
            name = input("변경하고 싶은 사람의 이름을 입력하세요 : ")
            change_Contact(contact_list, name)
        
        # 연락처 검색
        elif menu == 5:
            name = input("검색하고 싶은 사람의 이름을 입력하세요 : ")
            search_Number(contact_list, name)
        
        # 비밀친구?!?
        elif menu == 77:
            while secretmenu != 9 :
                secretmenu = BestshowMenu()
                
                if secretmenu == 1 :
                    print_contact(bestcontact_list)
                    
                elif secretmenu == 2:
                    name = input("비밀 친구로 등록할 사람의 이름을 입력하세요 : ")
                    Bestcontact = add_Bestfriends(contact_list, name)
                    # contact_list.append(Bestcontact)
                    bestcontact_list.append(Bestcontact)
                
                elif secretmenu == 3:
                    name = input("비밀 친구를 해제 할 사람의 이름을 입력하세요 : ")
                    del_Bestfriends(bestcontact_list, name)
                
                elif secretmenu == 4:
                    name = input("변경할 정보가 있는 비밀 친구의 이름을 입력하세요 : ")
                    change_Bestfriends(bestcontact_list, name)
                    
                elif secretmenu == 5:
                    name = input("검색하고 싶은 사람의 비밀 친구의 이름을 입력하세요 : ")
                    search_Bestfriends(bestcontact_list, name)
            
        # 연락처 저장
        elif menu == 9 :
            saveContact(contact_list)
            
            


##########실행하기 ##########
run()

# People1 = Person('박영진','01040528190') 
# People2 = Person("박영진","01040528190")

# if People1 == People2 :
#     print("같은 사람입니다")