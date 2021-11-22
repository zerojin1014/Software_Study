def solution1(year, month) :

#     # year 연 수 2021
#     # month 월 수 10

    if year < 0 or (month < 0 or month >= 13) :
        return False

    elif (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
        

# year = int(input("년도"))
# month = int(input("월"))

# if year < 0 or (month <= 0 or month >= 13):
#     print(0)

# elif (year % 4 == 0) and (year % 100 != 0 ) or (year % 400 == 0) :
#     if month in [1,3,5,7,8,10,12] :
#         print(31)
#     elif month in [4,6,9,11]:
#         print(30)
#     else:
#         print(29)

# else :
#     if month in [1,3,5,7,8,10,12] :
#         print(31)
#     elif month in [4,6,9,11]:
#         print(30)
#     else:
#         print(28)

def solution(year, month):
    answer = 0

    if year < 0 or (month <=0 or month >= 13):
        return 0

    elif (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        if month in [1,3,5,7,8,10,12]:
            return(31)
        elif month in [4,6,9,11]:
            return(30)
        else :
            return(29)

    else :
        if month in [1,3,5,7,8,10,12] :
            return(31)
        elif month in [4,6,9,11]:
            return(30)
        else:
            return(28)


