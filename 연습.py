answer = 0
i=0
j = 0
mul= int(input())
limit= int(input())

if mul <= 0 :
    print(0)
    

else :
    for i in range (1,limit+1):
        if i % mul == 0 :
            j += 1
            print(i,j)
        
    print(j)



