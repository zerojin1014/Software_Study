x = int(input("x : "))
y = int(input("y : "))


try :
    z= x/y
except ZeroDivisionError as e:
    print(e)
    print("0으로 나누는 경우는 제외합니다.")


try : 
    ''''''
except ValueError :
    print("다시")
else :
    print("")

try : 
    ''''''
except IOError :
    print("다시")
else :
    print("")

