#takes output of align.sh, changes it from a fastq to a fasta, then fills in ns
#ns are taken from the reference genome at the same location
#indels are removed in the vcutils step to ensure direct synteny
#usage: fakeparent.py input.fq refparent.fa output.fa 
#example usage: fakeparent.py fake1.fq parent1_ref.fa fakedp2.fa

import Bio
import sys

SeqIO.convert(sys.argv[1], "fastq-illumina", "tempfa.fa", "fasta")

handle = open(sys.argv[2], "rU")
refrecords = list(SeqIO.parse(handle, "fasta"))
handle.close()

handle = open("tempfa.fa", "rU")
mappedrecords = list(SeqIO.parse(handle, "fasta"))
handle.close()

filetowrite=open(sys.argv[3], 'a')

for chromosome in range(len(mappedrecords)):
	print(">",mappedrecords[chromosome].id,file=filetowrite)
	for base in range(len(mappedrecords[chromosome].seq)):
		if mappedrecords[chromosome].seq[base]=="n":
			print(refrecords[chromosome].seq[base].upper(),sep="",file=filetowrite,end="")
		else:
			print(mappedrecords[chromosome].seq[base].upper(),sep="",file=filetowrite,end="")
		lastbasedone=base
	if len(mappedrecords[chromosome].seq)==len(refrecords[chromosome].seq):
		break
	else:
		print(mappedrecords[chromosome].seq[lastbasedone:].upper(),sep="",file=filetowrite)

filetowrite.close()