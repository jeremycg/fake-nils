fake-nils
=========

For two given genomes, resticts one genome based on a MseI digest, fakes fastq reads, then maps to other genome.
Mapping can be done with bwa or stampy to allow more divergence. Outputs are made back into a parental genome using vcfutils.
No indels are included - this allows a simple syntenic genome. Used to create a "fake" syntenic genome for further analysis on the msg pipeline.

This is in general a terrible idea, but useful when one genome is of very poor quality and synteny, even forced, will help analysis.



Todo:

Create fake NILs from the given parental genomes - can we detect introgressions?

Some sensible double checking of reads - some of out reads will come from places that do not cut in both genomes - can we filter these out, so only "informative" reads are mapped?
