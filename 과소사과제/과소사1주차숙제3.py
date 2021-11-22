# 자동 판매기를 시뮬레이션하는 프로그램을 작성한다. 자동판매기에서 물건을 제공한 후
# 거스롬돈을 큰 지폐와 화폐 단위 금액을 다음 화폐단위로 단계 별로 지불하는 프로그램이다.
# 첫 parameter 는 물건 값, 두번째 parameter는 사용자가 넣은 돈의 총합이다.
# 10000원, 5000원, 1000원, 500원, 100원, 50원, 10원짜리 동전을 사용한다.
# 거스름돈의 총 화폐의 개수를 계산하여 반환하시오.
# 단 물건값보다 사용자의 입력 금액이 작은 경우는 사용자에게 입력 금액을 반환하여 줍니다.


# A = int(input())
# B = int(input())
# C = A - B

# # 50000원 -33340원 = 16660원 
# # 만원 1장, 오천원 1장, 천원 1장, 오백원 1개, 백원1개, 50원1개, 10원 1개 = 7개

def solution(itemPrice, money):
    count = 0
    A = int(money - itemPrice)

    coin_type = [10000,5000,1000,500,100,50,10]

    if itemPrice > money :
        for j in coin_type:
            count += money//j
            money %= j
            print(money,count)

    else:
        for i in coin_type :
            count += A//i
            A %= i
            print(A,count)
    
    return count

print(solution(52510,2470))



#     count = 0
#     A = int(money - itemPrice) 
#     coin_types = [10000,5000,1000,500,100,50,10,1]

#     if itemPrice > money :
#         return money

#     else :
#         for i in coin_types:
#             count += A//i
#             A %= i
#         return count

    

# def solution(itemPrice, money):
#     answer = ''

#     if itemPrice > money :
#         C = money
#         N1 = C // 10000; C %= 10000
#         N2 = C // 5000; C %= 5000
#         N3 = C // 1000; C %= 1000
#         N4 = C // 500; C %=500
#         N5 = C // 100; C %=100
#         N6 = C // 50; C%=50
#         N7 = C // 10
#         N = N1+N2+N3+N4+N5+N6+N7
#         return N
#     else :
#         C = int(money - itemPrice)
#         N1 = C // 10000; C %= 10000
#         N2 = C // 5000; C %= 5000
#         N3 = C // 1000; C %= 1000
#         N4 = C // 500; C %=500
#         N5 = C // 100; C %=100
#         N6 = C // 50; C%=50
#         N7 = C // 10
#         N = N1+N2+N3+N4+N5+N6+N7
#         return N

#     return answer



# N1 = C // 10000; C %= 10000
# N2 = C // 5000; C %= 5000
# N3 = C // 1000; C %= 1000
# N4 = C // 500; C %= 500
# N5 = C // 100; C %= 100
# N6 = C // 50; C %= 50
# N7 = C // 10


# if B > A :
#     print(A)

# else :
#     print(N1+N2+N3+N4+N5+N6+N7)

