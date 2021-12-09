
f = open("생물정보학/연습.fasta", 'r')
SeqList = f.readlines()
f.close()

# print(a[0])
# print(a[0][0])

i = 0
row = 1
count = ''
# print(SeqList)
# print(len(SeqList))

while row < len(SeqList):
    
    rowstring = SeqList[i]
    print(row, rowstring)
    # print(i, rowList , end="")

    if rowstring[0] == ">" :
        title1 = rowstring[1:].split("[")
        # title2 = title1[0].split(" ")
        # print(title)
        i += 1
        row += 1
        print(title2)
        continue
    
    if rowstring[0] != ">" and rowstring[0] != "\n" :
        line = rowstring.rstrip("\n")
        count += line
        i += 1
        row += 1
        continue
    
    # print(count, row)
    i += 1
    row += 1
