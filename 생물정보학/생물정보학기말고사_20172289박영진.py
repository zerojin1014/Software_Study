############################# 1번문제 ############################

# fas 파일과 py 파일이 같은 폴더내에 있다는 가정 하에
f = open("File_for_question1.fas", "r")
SeqList = f.readlines()
f.close

row = 1
sequence = ''
sequence_dict = {}

while row <= len(SeqList):

    rowindex = row - 1
    rowstring = SeqList[rowindex]

    if rowstring[0] == ">" :
        
        first_title = rowstring[1:].split(" [")
        
        spaceindex = first_title[0].find(" ")
        accNum = first_title[0][:spaceindex]
        proteinName = first_title[0][spaceindex+1:]

        orgainsm = first_title[1].rstrip("]\n")

        row += 1
        continue
    
    if rowstring[0] != ">" and rowstring[0] != "\n" :
        line= rowstring.rstrip("\n")
        sequence += line

        row += 1
        continue

    if rowstring[0] == "\n":
        sequence_dict[accNum] = [proteinName,orgainsm,sequence]
        sequence = ''

        row += 1
        continue

# sequence_dict 의 구성이 {accnNum, [proteinName,orgainsm,sequence]} 로 되게 구성함.
# 따라서 서열의 갯수가 dict의 len과 같다.

print(len(sequence_dict))


############################### 2번문제 ###################################

amino_acid = 'MFENITAAPADPILGLADLFRADERPGKINLGIGVYKDETGKTPVLTSVKKAEQYLLENETTKNYLGIDGIPEFGRCTQELLFGKGSALINDKRARTAQTPGGTGALRVAADFLAKNTSVKRVWVSNPSWPNHKSVFNSAGLEVREYAYYDAENHTLDFDALINSLNEAQAGDVVLFHGCCHNPTGIDPTLEQWQTLAQLSVEKGWLPLFDFAYQGFARGLEEDAEGLRAFAAMHKELIVASSYSKNFGLYNERVGACTLVAADSETVDRAFSQMKAAIRANYSNPPAHGASVVATILSNDALRAIWEQELTDMRQRIQRMRQLFVNTLQEKGANRDFSFIIKQNGMFSFSGLTKEQVLRLREEFGVYAVASGRVNVAGMTPDNMAPLCEAIVAVL'

total = len(amino_acid)
alanine = amino_acid.count('A')

percent = alanine / total * 100
percent = round(percent, 3)

print("아래의 아미노산 서열 에서 alanine 의 구성비율은",percent,"% (소수점 넷째 자리에서 반올림) 입니다.")