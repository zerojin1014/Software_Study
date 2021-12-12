# def vari_reset():
#     accNum = ''
#     proteinName = ''
#     orgainsm = ''
#     sequence = ''

#     return accNum, proteinName, orgainsm, sequence

f = open("sequence.fasta", "r")
SeqList = f.readlines()
f.close

# print(SeqList)


row = 1
sequence = ''
sequence_dict ={}

while row <= len(SeqList):
    
    # print(row, len(SeqList))
    
    rowindex = row -1
    rowstring = SeqList[rowindex]
    
    if rowstring[0] == ">" :
        
        first_title = rowstring[1:].split(" [")

        spaceindex = first_title[0].find(" ")
        accNum = first_title[0][:spaceindex]
        proteinName = first_title[0][spaceindex+1:]
        # print(first_title, accNum, proteinName)

        orgainsm = first_title[1].rstrip("]\n")
        # print(orgainsm)

        row += 1
        continue

    if rowstring[0] != ">" and rowstring[0] != "\n":
        line = rowstring.rstrip("\n")
        sequence += line

        row += 1
        continue

    if rowstring[0] == "\n" :
        sequence_dict[accNum] = [proteinName,orgainsm,sequence]
        sequence = ''

        row += 1
        continue


print(sequence_dict)