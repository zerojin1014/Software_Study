f = open("연습.fasta", 'r')
SeqList = f.readlines()
f.close()

# print(a[0])
# print(a[0][0])

row = 1
count = ''
Listlen = len(SeqList)
sequence_dic = {}
# print(SeqList)
print(len(SeqList))

while row <= Listlen :
    
    i = row -1

    rowstring = SeqList[i]
    print(row, rowstring)
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

print(sequence_dic) 