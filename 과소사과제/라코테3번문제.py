# 라코테 3번 문제

'''
369 게임을 프로그램하기
369 게임은 1부터 시작하여 숫자를 증가하면서, 입으로 말하거나 박수를 치는 게임이다.
숫자를 일씩 증가하면서 3,6,9가 들어가 있는 숫자에서는 입으로 그 숫자를 말하지 않고 박수를 치는 게임이다.
3,6,9 숫자가 없으면 그 숫자를 말한다.
[단 3의 배수라고 박수를 치는 것은 아니다. 즉 12에서는 박수를 치지 않는다.]

주어지는 int parameter를 받고, 1에서부터 이 parameter까지 숫자를 세면서, 그 수에 3,6,9 숫자가 들어가 있ㅇ므으로
박수를 친 총 횟수를 구하여 return하시오.

1에서는 박수를 치지 않고 숫자를 말한다.
2에서도 박수를 치지 않고 숫자를 말한다.
3에서는 박수를 한 번 친다.

33에서는 박수를 한 번 만 친다.
36에서도 박수를 한 번 친다.
'''

def three_six_nine(maxnum):
    '''
    count = 0 
    숫자는 1부터 maxnum+1 까지 쭉쭊쭉 진행하면서
    각각에서 3 6 9 가 들어있는지 판단해야함

    for num in range(1,maxnum+1):
        #num 은 정수형
        # s = str(num)
        if s in 
            count += 1
    return count
    '''

    count = 0 
    for num in range(1,maxnum+1):
        s = str(num)
        print(s)
        if ('3'in s) or ('6' in s) or ('9' in s) :
            count += 1
    return count

print(three_six_nine(40))

# # count = 0
# # n = int(input("몇번까지? : "))

# # for i in range(1,n+1):
# #     s = str(i)
# #     if ('3'in s) or ('6' in s) or('9' in s):
# #         count += 1
# # print(count)


# #### 369 갯수에 따라 박수 갯수가 변할 때 ###

n = int(input("몇번 까지? : "))

for i in range(1,n+1):
    count = 0
    s = str(i)
    
    for x in s :
        if (x=='3') or (x=='6') or (x=='9'):
            count += 1
            

    if count == 0 :
        print(i, end=' ')
    else :
        print(count*'짝', end=' ')
