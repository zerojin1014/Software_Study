menu = 0
friends = []
while menu != 9 :
    print("------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    
    menu = int(input("메뉴를 선택하시오 : "))
    
    if menu == 1 :
        print(friends)
    
    elif menu == 2: 
        name = input("친구 이름을 입력해주세용 : ")
        friends.append(name)
    
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력해주세요 : ")
        if del_name in friends :
            friends.remove(del_name)
        else :
            print("그런 이름은 없습니다.") 
    
    elif menu == 4:
        old_name = input("변경하고 싶은 이름을 입력해주세요 : ") 
        if old_name in friends :
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하세요 : ") 
            friends[index] = new_name 
        else :
            print("그런 이름은 없습니다.") 
           