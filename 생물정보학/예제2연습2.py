# f = open("pdb.txt", "r")

# line = None

# while line != '' :
#     line = f.readline()
#     print(line.rstrip("\n"))

# f.close

def get_info(line):
    atom_Name = line[12:16].strip()
    residue_Name = line[17:20].strip()
    residue_Number = line[22:26].strip()
    X_coor = line[30:38].strip()
    Y_coor = line[38:46].strip()
    Z_coor = line[46:54].strip()

    return atom_Name, residue_Name, residue_Number, X_coor, Y_coor, Z_coor

f = open("6enz.pdb", "r")
rowList = f.readlines()
f.close

import math
# CD1 LEU A 102 
# NZ  LYS A 314

for i in rowList :
    Atom, R_Name, R_Number, X, Y, Z = get_info(i)
    if Atom == 'CD1' and R_Name =='LEU' and R_Number =='102' :
        X1, Y1, Z1 = float(X), float(Y), float(Z)
    if Atom == 'NZ' and R_Name == 'LYS' and R_Number =='314' :
        X2, Y2, Z2 = float(X), float(Y), float(Z)

distance = math.sqrt((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2) 
distance = round(distance, 4)
print(distance)