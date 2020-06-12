import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import sys
    
data = pd.read_csv("bonds.csv")
print(data.head())

print("\n")
print("  Welcome to Plotter ")
print("  Here you can plot and your desired plot will be save to your directory")
print("\n")
def amino_acid():
    head1=np.array(data['LIG'])
    head2=np.array(data['Amino_acid'])
    bar(head1, head2)

def intrections():
    col1=np.array(data['Amino_acid'])   
    col2=np.array(data['Molecule'])
    bar_plot(col1, col2)

def bar(head1,head2):
    new=np.arange(len(head1))
    sns.barplot(new,list(head2),palette = 'hls',saturation = 10, label='Amino acid')   

    plt.xlabel('Ligand')
    plt.ylabel('amino acid')
    plt.title('amino acid')
    plt.legend(fontsize=10)
    plt.savefig("Amino_acid.png")
    plt.show() 

def bar_plot(col1,col2):
    new=np.arange(len(col1))
    sns.barplot(new,list(col2),palette = 'hls',saturation = 10, label='Intrections')   

    plt.ylabel('No of intrections')
    plt.xlabel('Amino acid')
    plt.title('Bar Plot')
    plt.legend(fontsize=10)
    plt.savefig("Intrections.png")
    plt.show() 
while True:
    choice=int(input("To plot number of Amino acids press 1\nTo plot number of Interctions press 2\nTo exit press 0\n"))
    if choice==1:
        amino_acid()
    elif choice==2:
        intrections()
    elif choice==0:
        sys.exit(0)


