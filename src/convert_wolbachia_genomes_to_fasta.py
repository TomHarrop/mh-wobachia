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

    main_contigs = [x for x in gb_list if x.name == 'NC_002978']
    alt_contigs = [x for x in gb_list if not x.name == 'NC_002978']
    main_fasta = 'output/genomes/wolbachia_wmel.fasta'
    alt_fasta = 'output/genomes/wolbachia_others.fasta'

    SeqIO.write(
        sequences=main_contigs,
        handle=main_fasta,
        format='fasta')

    SeqIO.write(
        sequences=alt_contigs,
        handle=alt_fasta,
        format='fasta')

if __name__ == '__main__':
    main()
