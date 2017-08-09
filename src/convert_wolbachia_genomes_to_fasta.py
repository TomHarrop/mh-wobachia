#!/usr/bin/env python3

from Bio import SeqIO
import copy
import gzip
import tompytools

def read_gff_gz(gbf):
    with gzip.open(gbf, 'rt') as f:
        gb = SeqIO.parse(f, 'gb')
        return(next(gb))

def rename_contigs(sr):
    my_seq_record = copy.deepcopy(sr)
    my_seq_record.name = ''
    my_seq_record.description = ''
    return(my_seq_record)

def main():
    genbank_files = tompytools.find_all(['genomic.gbff.gz'], 'output/genomes')
    gb_list = [read_gff_gz(x) for x in genbank_files]

    # separate main and ALT contigs
    main_contigs = [x for x in gb_list if x.name == 'NC_002978']
    alt_contigs = [x for x in gb_list if not x.name == 'NC_002978']

    # rename contigs to remove descprtion and name
    main_contigs_renamed = [rename_contigs(x) for x in main_contigs]
    alt_contigs_renamed = [rename_contigs(x) for x in alt_contigs]
    all_contigs_renamed = [rename_contigs(x) for x in gb_list]

    # generate list of ALT contig names
    alt_contig_names = [x.id for x in alt_contigs_renamed]

    # write fasta files
    all_fasta = 'output/genomes/wolbachia_all.fasta'
    main_fasta = 'output/genomes/wolbachia_wmel.fasta'
    alt_fasta = 'output/genomes/wolbachia_others.fasta'

    SeqIO.write(
        sequences=all_contigs_renamed,
        handle=all_fasta,
        format='fasta')

    SeqIO.write(
        sequences=main_contigs_renamed,
        handle=main_fasta,
        format='fasta')

    SeqIO.write(
        sequences=alt_contigs_renamed,
        handle=alt_fasta,
        format='fasta')

    # write alt contig names
    indexbase_alt = 'output/genomes/wolbachia_all.alt'
    with open(indexbase_alt, 'wt') as f:
        f.writelines('\n'.join(alt_contig_names))
        f.write('\n')

if __name__ == '__main__':
    main()
