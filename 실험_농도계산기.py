
#########################################
# 내가 가진 stock으로 원하는 농도 맞추기 #
#########################################

# 내가 가지고있는 농도  *  x = 희석하고 싶은 농도 * 원하는 볼륨
# 1 * x = 0.1 * 100마이크로리터

Mycon = float(input("나의 sample 농도값을 입력해주세요 _ ng/ul : "))
Wantcon = float(input("원하는 농도를 입력해주세요 _ ng/ul :  "))
WantVol = float(input("원하는 부피를 입력해주세요 _ ul : "))

MyVol = round(((Wantcon*WantVol)/Mycon),2)

print("")
print(MyVol," ul 만큼 넣어주면 완성!! 와~~ ! ")
print("DW는", WantVol-MyVol , "만큼 넣어주세요.\n")

