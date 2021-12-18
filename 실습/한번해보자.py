class info : 
    def __init__(self):
        self.name = ''
        self.number = ''
        self.e_mail = ''
        self.memo = ''

    def Clear(self):
        self.name = ''
        self.number = ''
        self.e_mail = ''
        self.memo = ''

class Person:
    def __init__(self):
        self.firendsDict = {}
        self.info = info()

    def add_Contact(self) : 
        
        # 이름 입력
        self.info.name = input("추가하고 싶은 친구 이름을 입력해주세요 : ")

        # 정보 입력
        info = []
        while True :    

            # 전화번호 입력
            self.info.number = input("전화번호를 입력하세요 : ")
            self.info.number = self.info.number.replace("-","")
            self.info.number = self.info.number.replace(" ","")
            
            Isonlynum = 1

            for i in self.info.number:
                if i not in ['0','1','2','3','4','5','6','7','8','9']:
                    Isonlynum = 0

            if Isonlynum == 0 :
                print("연락처 형식이 잘못되었습니다. 다시 입력해주세요.")
                continue

            else :
                info.append(self.info.number)
                print(self.info.name, self.info.number, "가 입력되었습니다.")
            
            # 이메일 입력
            option = input("이메일 입력 여부 (O/X) : ")
            if option == 'O' :
                self.info.e_mail = input("이메일을 입력해주세요 : ")
                print(self.info.name, self.info.e_mail, "(이)가 입력되었습니다.")
            else : 
                self.info.e_mail = '_'
            info.append(self.info.e_mail)
            
            # 메모 입력
            option = input("메모 입력 여부 (O/X) : ")
            if option == 'O' :
                self.info.memo = input("메모를 적어주세요. : ")
                print(self.info.name, self.info.memo, "가 입력되었습니다.") 
            else :
                self.info.memo = '_'
            info.append(self.info.memo)       
            print(self.info.name,"님의 연락처가 저장되었습니다.")

            print(info)
            contact = Person(self.info.name,info)
            return contact

contact = add