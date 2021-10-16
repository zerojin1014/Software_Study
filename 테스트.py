C = 15800

N1 = C // 10000
N2 = (C % 10000)// 5000
N3 = (C % 5000)// 1000
N4 = (C % 1000)// 500
N5 = (C % 500)// 100
N6 = (C % 100)// 50
N7 = (C % 50)// 10 


print(N1,N2,N3,N4,N5,N6,N7)

def solution(itemPrice, money):
    answer = ''
    C = money - itemPrice

    N1 = C // 10000; C %= 10000
    N2 = C // 5000; C %= 5000
    N3 = C // 1000; C %= 1000
    N4 = C // 500; C %=500
    N5 = C // 100; C %=100
    N6 = C // 50; C%=50
    N7 = C // 10

    if itemPrice > money :
        return money
    else :
        return (N1+N2+N3+N4+N5+N6+N7)

    return answer

def solution(itemPrice, money):
    answer = ''

    count = 0
    A = int(money - itemPrice) 
    coin_types = [10000,5000,1000,500,100,50,10,1]

    if itemPrice > money :
        return money

    else :
        for i in coin_types:
            count += A//i
            A%= i
        return count

    return answer