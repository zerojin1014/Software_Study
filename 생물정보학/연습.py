f = open("연습.fasta", 'r')
line = None

while line != '':
    line = f.readline()
    print(line.rstrip("\n"))

f.close()
