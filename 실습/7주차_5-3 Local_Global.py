# 지역 변수와 전역 변수
# 함수 외부에 있으면 전역 변수
# 함수 내부에 있으면 지역 변수

def sub(x,y):
    global a
    
    a = 7
    x,y = y,x
    b = 3
    print(a, b, x, y)
    
a,b,x,y = 1,2,3,4
sub(x,y)
print(a,b,x,y)

# 7 3 4 3
# 7 2 3 4

def sub(mylist):
    
    mylist = [1,2,3,4]
    print("함수 내부에서의 mylist : ", mylist)
    return

mylist =[10,20,30,40];
sub(mylist)
print("함수 외부에서의 mylist : ", mylist)