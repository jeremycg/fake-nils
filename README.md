fake-nils
=========

For two given genomes, resticts one genome based on a DraI digest, fakes fastq reads, then maps to other genome.
Mapping can be done with bwa or stampy to allow more divergence. Outputs are made back into a parental genome using vcfutils.
No indels are included - this allows a simple syntenic genome.
Used to create a "fake" syntenic genome for further analysis on the msg pipeline.
