def get_info(line):
    atom_name = line[12:16].strip()
    residue_name = line[17:20].strip()
    residue_number = line[22:26].strip()
    x_coor = line[30:37].strip()
    y_coor = line[38:46].strip()
    z_coor = line[46:54].strip()
    
    return atom_name, residue_name, residue_number, x_coor, y_coor, z_coor

import math

f = open("6enz.pdb", 'r')
a = f.readlines()
f.close()

# CD1 LEU A 102 
# NZ  LYS A 314

for i in a:
    A_number, R_name, R_number, X, Y, Z = get_info(i)
    if A_number == 'CD1'and R_name == 'LEU' and R_number == "102" :
        X1 , Y1 ,Z1 = float(X),float(Y),float(Z)
    if A_number == 'NZ'and R_name == 'LYS' and R_number == "314" : 
        X2 , Y2 ,Z2 = float(X),float(Y),float(Z)

distance = math.sqrt((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2)

distance_round = round(distance, 3)

print(distance_round)
'''
13 - 16 Atom name Atom name.
17 Character altLoc Alternate location indicator.
18 - 20 Residue name resName Residue name.
22 Character chainID Chain identifier.
23 - 26 Integer resSeq Residue sequence number.
27 AChar iCode Code for insertion of residues.
31 - 38 Real(8.3) x Orthogonal coordinates for X in Angstroms.
39 - 46 Real(8.3) y Orthogonal coordinates for Y in Angstroms.
47 - 54 Real(8.3) z Orthogonal coordinates for Z in Angstroms.
'''