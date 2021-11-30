# 무명 함수
# 무명 함수는 이름은 없고 몸체만 있는 함수이다.
# 파이썬에서 무명 함수는 lambda 키워드로 만들어 진다.

# lambda 인수1, 인수2 : 수식
# 예제

sum = lambda x, y : x+y

print(sum(10,20))
print(sum(30,40))

# 모듈 : 함수나 변수들을 모아 놓은 파일을 모듈(module)

import fibo

print(fibo.fib(1000))
print(fibo.__name__)

from fibo import*
fib(500)


# 성적 입력 후 sort하여 출력하는 예제

def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)
    
# if __name__ == "__main__":
#     main()

def readList():
    nlist = []
    flag = True
    while flag :
        number = int(input("숫자를 입력하세요 : "))
        if number < 0 :
            flag = False
        else : 
            nlist.append(number)
    return nlist

def processList(nlist):
    nlist.sort()
    return nlist

def printList(nlist):
    for i in nlist:
        print("성적= ", i)
        
main()