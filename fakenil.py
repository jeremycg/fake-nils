#imports parental genomes (made syntenic by previous pipeline)
#simulates a given cross based on a given number of loci per chromosome in parental genomes
#outputs a phased haploid genome sequence based on the simulated crosses
#gives a percentage of each parent
#usage: fakenil.py parent0.fa parent1.fa cross crossparent nloci output.fa

import sys
from Bio import SeqIO
from nilsim import cross,makeparent
import random

handle = open(sys.argv[1], "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()



nchrom=len(records)
nloci=int(sys.argv[5])
nilsim.nloci=nloci

parent0=nilsim.makeparent(nloci,nchro,0)
parent1=nilsim.makeparent(nloci,nchro,1)
nilsim.parent0=parent0
nilsim.parent1=parent1

print(sys.argv[3])
print(sys.argv[4])
print(nilsim.cross(sys.argv[3],sys.argv[4]))

print(nilsim.cross([1,1,1,1,1,1,"self","self","self","self","self","self"],parent0))
