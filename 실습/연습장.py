def LoadContact():
    infilename = "friendsList.txt"
    infile = open(infilename, "r")
    
    line = infile.readlines
    print(line)
    infile.close()
    
print(LoadContact())