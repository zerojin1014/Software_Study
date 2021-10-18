
# 가위바위 보 하나 뺴기


# 양수들의 합과 평균 값
# 사용자가 입력 하는 양수들의 합과 평균 값을 구하고 출력하라
# 사용자로부터 양의 정수를 입력받는다. 
# 양의 정수를 입력하시오를 반복하여 양수를 입력하도록 묻는다.
# 사용자가 그만 입력하고 싶으면 -1 값을 입력하도록 한다.
# 입력하는 수를 누적하여 더한 합과 평균을 구하고 출력한다.

count = 0
sum = 0
number = 1

while number != -1 :
    number = float(input("양의 수를 입력해주세요 (종료는 -1) : "))
    
    if number <= 0 and number != -1 :
        continue

    elif number > 0 :
        sum += number
        count += 1

print(sum,"입력된 갯수는 :",count)
if count>0 :
    print("평균 값은 :",sum/count)