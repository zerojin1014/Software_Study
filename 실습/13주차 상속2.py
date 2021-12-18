# class FourCal(Cal):
#     def __init__(self):
#         super().__init__(number1,number2)

######### 메소드 오버라이딩 #########
# 자식 클래스 메소드가 재정의

class Animal:
    def __init__(self,name=""):
        self.name = name
    
    def eat(self):
        print("동물이 먹고 있다")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    

    def eat(self):
        print("강아지가 먹고있따")

d = Dog()
d.eat()

# for car in cars:
#     pirnt( car.name +":"+ car.drive())