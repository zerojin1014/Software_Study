# f = open("생물정보학/sequence.fasta", 'r')
# SeqList = f.readlines()
# f.close()

# # print(a[0])
# # print(a[0][0])

# i = 0
# row = 0
# count = ''
# print(SeqList)
# print(len(SeqList))
# while row < len(SeqList):
    
#     rowList = SeqList[i]
#     # print(i, rowList , end="")

#     if rowList[0] == ">" :
#         title = rowList.split("[")
#         print(title)
#         i += 1
#         row += 1
#         continue
    
#     if rowList[0] != ">" and rowList[0] != "\n" :
#         line = rowList.rstrip("\n")
#         count += line
#         i += 1
#         row += 1
#         continue
    
#     print(count, row)
#     i += 1
#     row += 1


# '''
# FASTA FILE 한 줄당 리스트 하나
# 시작과 종료를 어떻게 아나?
# 시작은 >
# 종료는 \n\n
# if 시작 > 이면
# 해당 줄 > 제외하고 [1:] 다 하고.split(" ")
# 반복문
# 그 다음줄부터 removeGap = a.replace("\n","")
# count += removeGap
# '''

f = open("sequence.fasta", 'r')
SeqList = f.readlines()
f.close()

# print(a[0])
# print(a[0][0])

row = 1
count = ''
Listlen = len(SeqList)
sequence_dic = {}
# print(SeqList)
# print(len(SeqList))

while row <= Listlen :
    
    i = row -1

    rowstring = SeqList[i]
    # print(row, rowstring)
    # print(i, rowList , end="")

    if rowstring[0] == ">" :
        title = rowstring[1:].split(" [")
        
        accname = title[0]
        accorg_space = accname.find(' ')
        accNum = accname[:accorg_space]
        name =accname[accorg_space+1:]
        
        organism = title[1].rstrip(']\n')
       
        row += 1
        continue
    
    if rowstring[0] != ">" and rowstring[0] != "\n" :
        line = rowstring.rstrip("\n")
        count += line
        row += 1
        # print(count)
        continue

    if rowstring[0] == "\n" :
        sequence = count
        sequence_dic[accNum] = [name,organism,sequence]
        # print(sequence_dic) 
        accNum = ''
        name = ''
        organism = ''
        sequence = ''
        row += 1
        continue

    # # print(count, row)
    # i += 1
    # row += 1

print(sequence_dic),

acc = sequence_dic['EXL32019.1']
acc = sequence_dic['CAA0276519.1']

A = acc[0]
B = acc[1]
C = acc[2]
print(A)
print(B)
print(C)

total = len(C)
val = C.count('V')

percent = val / total *100
percent = round(percent,3)
print(percent)