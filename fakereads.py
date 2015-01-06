#takes the output from cut.py, and makes a .fastq with fake qualities and given coverage
#usage fakereads.py inputtxt outputfastq coverage quality
#example fakereads.py outp2.txt outp2.fastq 10 40

from Bio import SeqIO
import sys


def writefastq(sequence,outfile,coverage,quality):
	rec = sequence
	rec.letter_annotations["phred_quality"] = [quality] * len(sequence.seq)
	recs = [ rec ]
	for i in range(coverage):
		SeqIO.write(recs, outfile, "fastq")

handle = open(sys.argv[1], "rU")
handleout = open(sys.argv[2], "a")
for i in SeqIO.parse(handle, "fasta"):
	writefastq(i,handleout,int(sys.argv[3]),int(sys.argv[4]))
handle.close()
handleout.close()
