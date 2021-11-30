class FourCal:
    def __init__(self, first, second):   #매서드의 매개변수
        self.first = first              #메서드의 수행문
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    # 클래스 안에 구현된 함수는 다른말로 메서드라고 부른다.
    # 메서드의 첫 번째 매개변수 이름은 관례적
a = FourCal(4,2)
print(type(a))
print(a.add())

# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,3)
print(a.pow())
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 모든 기능 사용 가능

# 기존 클래스가 라이브러리 형태로 제공되거나 수정할 수 없을 때 사용

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return 0
        else : 
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())

# 모듈
'''
if __name__ == "__main__"을 사용하면 
C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는 
__name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
반대로 대화형 인터프리터나 다른 파일에서 이 모듈을
불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어
if문 다음 문장이 수행되지 않는다.
'''