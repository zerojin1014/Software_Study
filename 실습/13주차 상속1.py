# # class 자식클래스 (부모(수퍼)클래스) :
# #     생성자
# #     메소드

class Vechicle : 
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    #설정자 메소드
    def setMake(self,make):
        self.make = make
    
    #접근자 메소드
    def getMake(self):
        return self.make

    def getDesc(self):
        return "차량 = ("+str(self.make)+")"+\
            str(self.model)

class Truck(Vechicle):
    def __init__(self,make,model,payload):
        super().__init__(make,model)        ########### 중요
        self.payload = payload

    # 설정자 메소드
    def setPayload(self,payload):
        self.payload = payload

    # 접근자 메소드
    def getPayload(self):
        return self.payload 

def main():
    myTruck = Truck("Tisla","Model S",2000)
    myTruck.setMake("Tesla")
    myTruck.setPayload(2000)

    print(myTruck.getDesc())

print(main())


class Car :
    def __init__(self,speed):
        self.speed=speed
    def setSpeed(self,speed):
        self.speed = speed
    def getDesc(self):
        return "차량 =("+str(self.speed)+")"

class SportsCar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo

    def setTurbo(self,turbo):
        self.turbo = turbo

obj = SportsCar(100,True)
print(obj.getDesc())
obj.setTurbo(False)



