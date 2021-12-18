class Person :
    friends_num = {}

    def __init__(self,name,info):
        self.name = name
        self.info = info

    def print_info(self):
        print("Name : " + self.name)
        print("number : " + self.info[0])
        print("E-mail : " + self.info[1])
        print("memo : " + self.info[2]) 

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
        
        contact = Person(name,info)
        friends_num[name] = info
        print(name,"님의 연락처가 저장되었습니다.")
        return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def run ():
    contact_list =[]
    contact = addname()
    contact_list.append(contact)

    print_contact(contact_list)

run()