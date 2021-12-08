import math 

#공간에서 두 점 사이의 거리

X1,Y1,Z1 = 4.23, 2.34, 66.2
X2,Y2,Z2 = 3.21, 2.11, 57.6

A = math.sqrt((X1-X2)**2+(Y1-Y2)**2+(Z1-Z2)**2)
B = round(A,3)
print(B)