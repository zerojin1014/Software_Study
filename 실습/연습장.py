
PhoneNumber = input("전화번호를 입력하세요 : ")
PhoneNumber = PhoneNumber.replace("-","")
PhoneNumber = PhoneNumber.replace(" ","")
Phone_D = PhoneNumber.isdigit
print(PhoneNumber,Phone_D)
print(type(PhoneNumber),type(Phone_D))