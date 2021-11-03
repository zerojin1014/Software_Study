
# 가위바위 보 하나 뺴기


# 양수들의 합과 평균 값
# 사용자가 입력 하는 양수들의 합과 평균 값을 구하고 출력하라
# 사용자로부터 양의 정수를 입력받는다. 
# 양의 정수를 입력하시오를 반복하여 양수를 입력하도록 묻는다.
# 사용자가 그만 입력하고 싶으면 -1 값을 입력하도록 한다.
# 입력하는 수를 누적하여 더한 합과 평균을 구하고 출력한다.

sum = 0
count = 0
number = 1
while number != -1 :
    number = float(input("양의 수를 입력해주세요 (종료는 -1 ): " ))

    if number <=0 and number != -1 :
        continue

    elif number > 0 :
        sum += number
        count += 1

print(sum,"입력된 갯수는 : ",count)
if count > 0 :
    print("평균 값은 : ", sum/count)
# count = 0
# sum = 0
# number = 1

# while number != -1 :
#     number = float(input("양의 수를 입력해주세요 (종료는 -1) : "))
    
#     if number <= 0 and number != -1 :
#         continue

#     elif number > 0 :
#         sum += number
#         count += 1

# print(sum,"입력된 갯수는 :",count)
# if count>0 :
#     print("평균 값은 :",sum/count)


# 오늘이 일요일이면 , 100일 후는 무슨 요일인가?

year = int(input("년도는 ? : "))
month = int(input("월은 ? : "))
date = int(input("일은 ? : "))
yearday = 0
monthday = 0
dateday = 0

for i in range(1,year):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0 :
        day = 366
        yearday += day
                
        for j in range(1,month):
            if j in [1,3,5,7,8,10,12]:
                day = 31
                monthday += 31
            elif j in [4,6,9,11]:
                day =30
                monthday += 30
            else : 
                day =29
                monthday += 29

    else :
        day = 365
        yearday += day

        for j in range(1,month):
            if j in [1,3,5,7,8,10,12]:
                day = 31
                monthday += 31
            elif j in [4,6,9,11]:
                day =30
                monthday += 30
            else : 
                day =28
                monthday += 28

result = yearday + monthday + date-1

if result % 7 == 0 :
    print("Monday")
elif result % 7 == 1 :
    print("Tuseday")
elif result % 7 == 2 :
    print("Wednesday")
elif result % 7 == 3 :
    print("Thursday")
elif result % 7 == 4 :
    print("Friday")
elif result % 7 == 5 :
    print("Saturday")
elif result % 7 == 6 :
    print("Sunday")

print(yearday,monthday,date-1,result)

