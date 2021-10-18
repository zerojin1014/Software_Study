# 세 실수 중 큰 값은?

# a = float(input())
# b = float(input())
# c = float(input())

# print(max(a,b,c))


def solution(first, second, third):
    answer = ''
    if first >= second and first >= third :
        return first
    elif second >= first and second >= third :
        return second
    else:
        return third
    return answer

    