#!/usr/bin/env python3

from Bio import SeqIO
import gzip
import tompytools

def read_gff_gz(gbf):
    with gzip.open(gbf, 'rt') as f:
        gb = SeqIO.parse(f, 'gb')
        return(next(gb))

def main():
    genbank_files = tompytools.find_all(['genomic.gbff.gz'], 'output/genomes')
    gb_list = [read_gff_gz(x) for x in genbank_files]

    output_fasta = 'output/genomes/wolbachia_genomes.fasta'
    SeqIO.write(
        sequences=gb_list,
        handle=output_fasta,
        format='fasta')

if __name__ == '__main__':
    main()
