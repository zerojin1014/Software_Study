import random
a = random.randint(1,100)

print("숫자게임에 오신 것을 환영합니다.")
i = int(input("몇번만에 맞출래요?: "))

while True :
    n = int(input("1부터 100 사이의 숫자를 추측해보세요 : "))

    if n > a and i>0 :
        print("떙, 정답은 더 낮습니다. 다시 도전해보세요.\n")
        i -= 1
        print('기회는', i ,'번 남았습니다.')

    elif n < a and i>0:
        print("땡, 정답은 더 높습니다. 다시 도전해보세요.\n")
        i -= 1
        print('기회는', i ,'번 남았습니다.')
    elif n == a and i >0:
        print("정답입니다!!")
        break 
    elif i == 0 :
        print("기회는 없어요 탈락입니다 ㅋㅋ 수고요 ^^ ")

# 5번 내로 맞추면 아이스크림