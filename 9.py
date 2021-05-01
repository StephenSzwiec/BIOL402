import sys
from Bio import SeqIO


# parse FASTQ file into FASTA
def Fastq2Fasta(fastq):
    with open(fastq, 'r') as input_handle:
        with open("rosa9_output.fasta", 'w') as output_handle:
            SeqIO.convert(input_handle, "fastq", output_handle, "fasta")


def main():
    for arg in sys.argv[1:]:
        Fastq2Fasta(arg)


if __name__ == "__main__":
    main()
