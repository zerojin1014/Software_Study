### 예외처리 ZeroDivisionError

x = int(input("x : "))
y = int(input("y : "))

try :
    z= x/y
    # 예외가 발생할 수 있는 문장
except ZeroDivisionError as e:
    print(e)
    print("0으로 나누는 경우는 제외합니다.")
    # 예외를 처리할 수 있는 문장

### 예외처리 ValueError
while True :
    
    try :
        n = input("숫자를 입력하시오 : ")
        n = int(n)
        break
     
    except ValueError as e :
        print(e)
        print("정수가 아닙니다. 다시 입력하시오.")

print("정수 입력이 성공하였습니다! ")


## 예외처리 IOError
try : 
    ''''''
except IOError :
    print("다시")
else :
    print("")

### 다중 예외 처리 예제

try : 
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:       #위의 오류가 해결 되야 출력한다.
    print(e)
    
## try .. finally

def divide(m,n):
    try :
        result = m /n
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else :
        print("ZeroDivisionError 이외의 예외 발생")
    finally :
        print ("나눗셈 연산입니다.")

print(divide(3,0))
# '''
# finally 절은 try문 수행 도중 예외 발생 여부에 상관없이
# 항상 수행된다. '''

# #f = open('foow.txt', 'r')
# #
# #try :
# #    "무언갈 수행한다."
# #
# #except FileNotFoundError:
# #   pass
# #finally :
# #    f.close()

# # 오류 회피하기
# # 특정 오류가 발생할 경우 pass를 사용하여 통과하며 오류 회피


# ## 예외 만들기
# ## 예제 class 배우고

# '''파일은 텍스트 파일과 이진 파일로 나누어진다.
# 파일은 연 후에 입출력이 끝나면 반드시 닫아야 한다.

# 파일에서 데이터를 읽거나 쓰는 함수는 read()와 write() 함수이다.
# 텍스트 파일에서 한 줄을 읽으려면 for 루프를 사용한다.
# for line in readlines()

# 예외 처리는 오류가 발생했을 때 프로그램을 우아하게 종료하는 방법이다.
# try 블록과 except 블록으로 이루어진다.
# '''