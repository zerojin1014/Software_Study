#################### 9주차 내용 ##########################

a = "20211119Rainy"
date = a[:8]
weather = a[8:]
year = date[:4]
month = date[4:6]
day = date[6:]

print(a,date,weather,year,month,day)

a = '''>gi|12345678_hexokinase_[Escherichia coli]
MASEDRTYYUDFGEFQET'''
print(a)

b = a.split("\n")
print(b)

c = b[0]
print(c)

d= b[0][1:].split("_")
print(d)

gi_num = d[0]
print(gi_num)
function = d[1]
print(function)
source = d[2]
print(source)
source1 = source[1:-1]
print(source1)

