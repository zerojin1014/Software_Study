f = open("생물정보학/sequence.fasta", 'r')
SeqList = f.readlines()
f.close()

# print(a[0])
# print(a[0][0])

i = 0
row = 0
count = ''
print(len(SeqList))
while row < len(SeqList):
    
    rowList = SeqList[i]
    # print(i, rowList , end="")

    if rowList[0] == ">" :
        title = rowList.split("[")
        print(title)
        i += 1
        row += 1
        continue
    
    if rowList[0] != ">" and rowList[0] != "\n" :
        line = rowList.rstrip("\n")
        count += line
        i += 1
        row += 1
        continue
    
    print(count, row)
    i += 1
    row += 1


'''
FASTA FILE 한 줄당 리스트 하나
시작과 종료를 어떻게 아나?
시작은 >
종료는 \n\n
if 시작 > 이면
해당 줄 > 제외하고 [1:] 다 하고.split(" ")
반복문
그 다음줄부터 removeGap = a.replace("\n","")
count += removeGap
'''