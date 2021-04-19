import sys
import time
import subprocess
# Entrez: https://ncbi.nlm.nih.gov/dbvar/content/tools/entrez
from Bio import Entrez
from Bio import SeqIO
from Bio import AlignIO
from Bio.Emboss.Applications import NeedleCommandline
# call entrez_setup to set api_key and email for RFC2606
from entrez_api import entrez_setup


# return the list of databases
def entrez_dblist():
    entrez_setup()
    handle = Entrez.einfo()
    record = Entrez.read(handle)
    return record


# return attributes of a database, given its name
def entrez_dbattribs(this_db):
    entrez_setup()
    handle = Entrez.einfo(db=this_db)
    record = Entrez.read(handle)
    fields = ""

    for field in record["DbInfo"]["FieldList"]:
        fields += ("%(FullName)s" % field)
    return fields


# parse words in file into vector of strings
def parseInput(fileName):
    eof = False
    temp = ""
    data = []

    with open(fileName) as f:
        while eof is not True:
            temp = f.readline()
            if temp == '':
                eof = True
                break
            for i in temp.split():
                data += [i]
    return data


# wrapper for accession search: returns fasta files
def entrez_acc_to_fasta(accession):
    entrez_setup()
    handle = Entrez.esearch(db="nucleotide", term=accession, retmax="40")
    handle2 = Entrez.efetch(db="sequences", id=(Entrez.read(handle)["IdList"]), rettype="fasta", retmode="text")
    return SeqIO.parse(handle2, "fasta")


# wrapper for accession search: returns an ID
def entrez_acc_to_id(accession):
    entrez_setup()
    handle = Entrez.esearch(db="nucleotide", term=accession, retmax="40")
    return Entrez.read(handle)["IdList"]


# wrapper for setting up NW EMBOSS
# NOTE: for whatever reason this needs two IDs instead of fasta sequences
# TODO: it also uses an external txt file, which is disgusting
# all of the setup for NW EMBOSS is here
def nw_by_id(id1, id2):
    needle_cline = NeedleCommandline()
    needle_cline.asequence = id1
    needle_cline.bsequence = id2
    needle_cline.outfile = "rosalind_5_output.txt"
    needle_cline.gapopen = 10
    needle_cline.gapextend = 1
    needle_cline.endopen = 10
    needle_cline.endextend = 1
    needle_cline.endweight = True
    needle_cline()


# magic happening here
def main():
    entrez_setup()
    ids = []
    seqs = []

    for arg in sys.argv[1:]:
        strings = parseInput(arg)
    for i in strings:
        time.sleep(.5)
        print(i)
        ids += entrez_acc_to_id(i)
        seqs += entrez_acc_to_fasta(i)
    for j, r in enumerate(seqs):
        with open(ids[j], 'w') as f:
            SeqIO.write(r, f, 'fasta')

    nw_by_id(ids[0], ids[1])

    with open('rosalind_5_output.txt') as filestream:
        output = filestream.readlines()
    for line in output:
        if "Score:" in line:
            print(line)


if __name__ == "__main__":
    main()
