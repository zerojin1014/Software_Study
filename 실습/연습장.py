
friends =[]

old_name = input("변경하고 싶은 이름을 입력해주세요 : ") 
if old_name in friends :
    index = friends.index(old_name)
    new_name = input("새로운 이름을 입력하세요 : ") 
    friends[index] = new_name 
