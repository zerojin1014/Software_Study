import random
a = random.randint(1,100)

print("숫자게임에 오신 것을 환영합니다.")

while True :
    n = int(input("1부터 100 사이의 숫자를 추측해보세요 : "))

    if n > a :
        print("떙, 정답은 더 낮습니다. 다시 도전해보세요.\n")
    elif n < a :
        print("땡, 정답은 더 높습니다. 다시 도전해보세요.\n")
    elif n == a :
        print("정답입니다!!")
        break 
