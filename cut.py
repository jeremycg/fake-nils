#reads the genome, cuts on TTAA, size selects, then outputs a .txt file of all the fragments
#usage - cut.py genomein txtout minsize maxmize
#example cut.py parent2_ref.fa outp2.txt 100 350
import sys
from Bio import SeqIO

def cutme(seq,seqid,mindist,maxdist,outputfile):
	counter=-1
	filetowrite=open(outputfile, 'a')
	while counter<len(seq)-3:
		count2=seq.find("TTAA",counter+1)
		if count2==-1:
			break
		if count2-counter > mindist and count2-counter < maxdist:
			if counter==-1:
				countprint=0
			else:
				countprint=counter
			print(">",str(seqid),str(counter),str(count2), file=filetowrite,sep='_')
			print(seq[countprint:count2+4],file=filetowrite)
		counter=count2
	filetowrite.close()



handle = open(sys.argv[1], "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
for i in records:
    i.seq=i.seq.upper()
    cutme(i.seq,i.id,int(sys.argv[3]),int(sys.argv[4]),sys.argv[2])