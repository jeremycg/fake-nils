#takes output of align.sh, changes it from a fastq to a fasta, then fills in ns
#ns are taken from the reference genome at the same location
#indels are removed in the vcutils step to ensure direct synteny
#usage: fakeparent.py input.fq refparent.fa output.fa
#example usage: fakeparent.py fake1.fq parent1_ref.fa fakedp2.fa

from Bio import SeqIO
from nilsim import parental
import sys

SeqIO.convert(sys.argv[1], "fastq-illumina", "tempfa.fa", "fasta")
parental("tempfa.fa",sys.argv[2],sys.argv[3])
