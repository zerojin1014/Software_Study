# 범위 내의 피보나치 수열의 마지막 값을 구하는 프로그램을 작성하세요.
# 주어진 parameter 값 내에서 피보나치 수열을 생성할 때 가장 마지막 수를 return 하시오.

# 예) 1000의 값을 주면, 피보나치 수열을
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# 이므로, 마지막 값인 987을 반환한다.

num = int(input("범위를 입력하세요 : "))
A = 0
B = 1
List=[]


for i in range(10):
    C = A + B # C = 3
    List.append(C)
    A = B + C # A = 5
    List.append(A)
    B = C + A # B = 8
    List.append(B)
    

    print(List)



# F = 


# if i <= num :
#     print(i) 