#takes the output from cut.py, and makes a .fastq with fake qualities and given coverage
#usage fakereads.py inputtxt outputfastq coverage quality
#example fakereads.py outp2.txt outp2.fastq 10 40

import Bio
import sys


def writefastq(sequence,outfile,coverage,quality):
	rec = sequence
	rec.letter_annotations["phred_quality"] = [quality] * len(sequence.seq)
	recs = [ rec ]
	handle = open(outfile, "a")
	for i in range(coverage):
		SeqIO.write(recs, handle, "fastq")

handle = open(sys.argv[1], "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
for i in records:
	writefastq(i,sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
