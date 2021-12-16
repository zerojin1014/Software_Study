class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None

    def __str__(self):
        return self.name + "" + str(self.pet)

dog1 = Dog("dog1")
print(dog1)

person1 = Person("홍길동")
print(person1)

person1.pet =dog1
print(person1.pet)

print(person1)