#!/bin/sh
#this should loop everything together
#usage:
#bash wholething.sh badparent.fa minsize maxsize coverage quality goodparent method output.fa
#example
#bash wholething.sh parent2_ref.fa 100 350 10 40 parent2_ref.fa bwa fakeout.fa
#makes several tempout files - these can be deleted but are left in for troubleshooting

python cut.py $2 tempout.txt $3 $4
python fakesreads.py tempout.txt tempout.fastq $5 $6
bash align.sh tempout.fastq $7 $8 tempout.fq
python fakeparent.py tempout.fq $7 $9