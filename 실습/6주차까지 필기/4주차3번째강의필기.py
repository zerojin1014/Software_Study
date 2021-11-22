#######################  4주차 3 #############################
# (Revisit)

# https://dojang.io/mod/page/view.php?id=2460

# 컴퓨터는 정보를 비트로 표시
# 8비트 (bit) -> 1바이트 (Byte), 32/64 비트 -> 1워드(word)


# 비트 논리 연산자      >> 공부필요
# & : 비트 논리곱   둘 다
# \ : 비트 논리합
# ^ : 비트 XOR
# ^ : 캐롯(carrot) 
# XOR : Exclusive OR 
# ~ : 비트 논리 부정  


a = 15
b = 5
print (bin(15),"\n",bin(5))
print(a&b, bin(a&b)) # a와 b 둘다 1이어야 1
print(a|b, bin(a|b)) # a와 b 둘 중 하나만 1이여도 1
print(a^b, bin(a^b)) # a와 b 다르면 1 같으면 0
# a^b^a=b
print(~a, bin(~a)) # 0을 1로 1을 0으로

print(int('1010',2))

# 비트 쉬프트 연산자 ??
# >> 오른쪽 shift   각 비트를 오른쪽으로 옮긴다. #2로 나누는 효과
# << 왼쪽 shift     각 비트를 왼쪽으로 옮긴다. #2를 곱하는 효과
print(a>>2,bin(a>>2))
print(b<<2,bin(b<<2))

# 비트마스크 ??
print("")
x = 4
print(bin(x))
for i in range(3):
    print("1st bit of %d" %x, 1 & (x>>i))

# E - 표기법 
y = 12300000000             #1.230000e+10 은 10**(10)
                            #1.23e-09 은 10**(-9)
print('%e' %y)
y = 0.00000000123
print(y)

# # 10진수 -> 2진수 변환 ?

print(bin(2017))
print(int('1010',2))

#######################  4주차 4 #############################
# (Revisit)

# string ='abcdef'
# print(string[0:4])

# string[3] = 'z'  >>>>>>> string은 불변 타입 immutable 

# 불변 데이터 타입 : tuple , string
# 가변 데이터 타입 : list , dictionary, set

# Boolean Data > True 는 1 False는  0   bool() : boolean으로 변환
# chr(숫자) : 숫자에 해당하는 아스키 (ascii) 문자로 변환
# ord(문자) : 아스키 문자에 해당하는 숫자로 변환
# Type() : 변수가 가리키는 객체 (object)의 타입을 알고 싶을 때 사용함

