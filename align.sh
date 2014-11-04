#!/bin/sh
#align reads (in this case, fake reads) to a parental genome
#usage is bash align.sh reads.fq ref.fa method out.fq
#depends on bwa and stampy, also vcfutils.pl I'm calling this from the current dir as it's not installed on my server
#example useage: bash align.sh outp2.fastq parent1_ref.fa bwa fake1.fq

if [ $3 = "bwa" ]
then
	bwa index $2
	bwa mem -t 4 $2 $1 > aln-se.sam
elif [ $3 = "stampy" ]
then
	stampy.py -G hashed $2
	stampy.py -g hashed -H hashed
	stampy.py -g hashed -h hashed -M $1 --substitutionrate=0.05 -o aln-se.sam -t 4
else
echo "invalid method"
fi

samtools view -S -b -o se-aln.bam aln-se.sam
samtools sort se-aln.bam se-alnsort
samtools mpileup -ugf $2 se-alnsort.bam | bcftools view -bvcg - > var.raw.bcf
bcftools view var.raw.bcf > raw.vcf
samtools mpileup -uf $2 se-alnsort.bam | bcftools view -cg - | perl vcfutils.pl vcf2fq > $4
