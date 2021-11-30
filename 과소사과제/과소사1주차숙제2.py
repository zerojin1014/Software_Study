# 세 실수 중 큰 값은?

# a = float(input())
# b = float(input())
# c = float(input())

# print(max(a,b,c))


def solution(first, second, third):
    if first >= second and first >= third :
        return first
    elif second >= third and second >= third :
        return second
    elif third >= second and third >= first :
        return third

print(solution(3.52,123.52,213.22))
    










    # if first >= second and first >= third :
    #     return first
    # elif second >= first and second >= third :
    #     return second
    # else:
    #     return third
    # return answer

    