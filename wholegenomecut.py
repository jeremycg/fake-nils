#reads the genome, cuts in 150bp fragments then outputs a .txt file of all the fragments
#usage - cut.py genomein txtout
#example cut.py parent2_ref.fa outp2.txt
import sys
from Bio import SeqIO

def cutme2(seq,seqid,outputfile):
  counter=0
  filetowrite=open(outputfile, 'a')
  while counter<len(seq)-150:
    countprint=counter
    print(">",str(seqid),str(counter), file=filetowrite,sep='_')
    print(seq[countprint:countprint+150],file=filetowrite)
    counter+=10
  filetowrite.close()



handle = open(sys.argv[1], "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
for i in records:
    i.seq=i.seq.upper()
    cutme2(i.seq,i.id,sys.argv[2])
