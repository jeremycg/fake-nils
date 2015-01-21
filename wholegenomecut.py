#reads the genome, cuts in 150bp fragments then outputs a .txt file of all the fragments
#usage - cut.py genomein txtout
#example cut.py parent2_ref.fa outp2.txt
import sys
from Bio import SeqIO

def cutme2(seq,seqid,outputconnection):
  counter=0
  while counter<len(seq)-150:
    countprint=counter
    print(">",str(seqid),str(counter), file=outputconnection,sep='_')
    print(seq[countprint:countprint+150],file=outputconnection)
    counter+=10



handle = open(sys.argv[1], "rU")
handleout = open(sys.argv[2], "w")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
for i in records:
    i.seq=i.seq.upper()
    cutme2(i.seq,i.id,handleout)
handleout.close()
