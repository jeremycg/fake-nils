#imports parental genomes (made syntenic by previous pipeline)
#simulates a given cross based on a given number of loci per chromosome in parental genomes
#outputs a phased haploid genome sequence based on the simulated crosses
#gives a percentage of each parent
#usage: fakenil.py parent0.fa parent1.fa cross crossparent nloci output.fa barcode

import sys
from Bio import SeqIO
from nilsim import combinegametes,makeparent,makegametes,crosschrom,percentageril,convertlens,makenil,cutme,writefastq
import random

handle = open(sys.argv[1], "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

def cross(list1,parent,sibling=0):#function of croses to do, the parent and a sibling
        if len(list1)==0:#if all our crosses are done, return the offspring
                return(parent)
        elif(len(list1)==1 or list1[1]!="sib"):
                if(list1[0])==1:#if the cross is 1, backcross to parent 1
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent1))))
                elif(list1[0])==0:#if the cross is 0, backcross to parent 0
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent0))))
                elif(list1[0])=="sib":#if the cross is sib, sib mate
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(sibling))))
                elif(list1[0])=="self":#if the cross is self, self
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent))))
        elif(list1[1]=="sib"):
                if(list1[0])==1:#if the cross is 1, backcross to parent 1
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent1)),combinegametes(makegametes(parent),makegametes(parent1))))
                elif(list1[0])==0:#if the cross is 0, backcross to parent 0
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent0)),combinegametes(makegametes(parent),makegametes(parent0))))
                elif(list1[0])=="sib":#if the cross is sib, sib mate
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(sibling)),combinegametes(makegametes(parent),makegametes(sibling))))
                elif(list1[0])=="self":#if the cross is self, self
                        return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent)),combinegametes(makegametes(parent),makegametes(parent))))



nchrom=len(records)
nloci=int(sys.argv[5])

parent0=makeparent(nloci,nchrom,0)
parent1=makeparent(nloci,nchrom,1)

fakenil=cross(eval(sys.argv[3]),eval(sys.argv[4]))
print(crosschrom(fakenil))
print(percentageril(fakenil))
makenil(sys.argv[1],sys.argv[2],convertlens(crosschrom(fakenil),records,10000),"nilgenome.fa")
cutme("nilgenome.fa",100,350,"nilfragments.fa",sys.argv[7])
writefastq("nilfragments.fa",sys.argv[6],5,40)
