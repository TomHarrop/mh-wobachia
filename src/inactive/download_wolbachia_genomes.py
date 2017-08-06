#!/usr/bin/env python3

from Bio import SeqIO
import gzip
import os
import shutil
import tempfile
from urllib.request import urlopen


# download function
def download_and_parse_fasta(genome_ftp):
    dl_tempfile = tempfile.mkstemp(suffix='.fna.gz')[1]
    fa_tempfile = tempfile.mkstemp(suffix='.fasta')[1]
    # download the genome
    with urlopen(genome_ftp) as req:
        with open(dl_tempfile, 'wb') as f:
            shutil.copyfileobj(req, f)
    # unzip
    with gzip.open(dl_tempfile, 'rb') as f_in:
        with open(fa_tempfile, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    # read
    fa_handle = SeqIO.parse(fa_tempfile, 'fasta')
    fa = next(fa_handle)
    # tidy
    os.remove(dl_tempfile)
    os.remove(fa_tempfile)
    return(fa)


def main():
    # files to download
    GCF_000022285 = "ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/022/285/"
    GCF_000022285 += "GCF_000022285.1_ASM2228v1/"
    GCF_000022285 += "GCF_000022285.1_ASM2228v1_genomic.fna.gz"

    GCF_000376605 = "ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/376/605/"
    GCF_000376605 += "GCF_000376605.1_ASM37660v1/"
    GCF_000376605 += "GCF_000376605.1_ASM37660v1_genomic.fna.gz"

    GCF_000008025 = "ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/008/025/"
    GCF_000008025 += "GCF_000008025.1_ASM802v1/"
    GCF_000008025 += "GCF_000008025.1_ASM802v1_genomic.fna.gz"

    wolbachia_genomes = [GCF_000022285, GCF_000376605, GCF_000008025]

    # run downloads
    wolbachia_fasta = [download_and_parse_fasta(x) for x in wolbachia_genomes]

    output_fasta = 'data/wolbachia_genomes.fasta'
    SeqIO.write(
        sequences=wolbachia_fasta,
        handle=output_fasta,
        format='fasta')

if __name__ == '__main__':
    main()
