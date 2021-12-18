class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return '{0}: {1}'.format(self.name, self.age)


def main():
    p = Person('James', 23)
    print(p)  # James: 23  --> __str__ 호출


main()