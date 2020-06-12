from Bio.PDB import *
import os
import subprocess
import pandas as pd
import numpy as np

pdbl = PDBList() 
new1=input("Enter PDB id: ")
file=pdbl.retrieve_pdb_file(new1, pdir = '.', file_format = 'pdb')

records = []
with open(file, "r") as f:
    for line in f: 
        if "HETATM" not in line and "CONECT" not in line : 
            records.append(line)
        if 'ATP' in line:
            line = line.replace('ATP', 'LIG')
            records.append(line)
            
with open("new.pdb", "w") as f: 
    for line in records: 
        f.write(line)


def vmd():
    a = list(("vmd new.pdb -e command.txt").split(" "))
    subprocess.Popen(a)
    
    subprocess.run('start' ,shell=True)
vmd()  