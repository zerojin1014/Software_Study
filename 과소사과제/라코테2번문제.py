# prime 값 구하기
# from datetime import datetime

num =int(input("정수를 입력하세요 : "))
prime_num = []

for n in range(2,num+1):
    divisor = 0
    if n <= 1:
        False
    for x in range(2,n):
        if n % x == 0 :
            divisor = 1
            break
    if divisor == 0 :
        prime_num.append(n)
    
print("소수의 개수는", len(prime_num)," 개 입니다.")
print("소수는", prime_num)

# start =datetime.now()
# end = datetime.now()
# print('걸린 시간 : ',end-start) # 현재 시간 - 함수 시작 시간

