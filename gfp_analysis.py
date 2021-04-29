# import from Biopython for protein analysis
from Bio.PDB import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis


# GFP sequence import and inital analysis
seq = "MRKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFARYPDHMKQHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITHGMDELYKRPAANDENYAASV"
analyzed_seq = ProteinAnalysis(str(seq))


# display some information about GFP
print(len(seq)) # 251 AAs long
print(analyzed_seq.count_amino_acids())
# {'A': 14, 'C': 2, 'D': 19, 'E': 17, 'F': 12, 'G': 22, 'H': 10, 'I': 11, 'K': 20, 'L': 20, 'M': 5, 'N': 15, 'P': 11, 'Q': 8, 'R': 8, 'S': 10, 'T': 18, 'V': 18, 'W': 1, 'Y': 10}
print(analyzed_seq.molecular_weight()) # 28 kDa
print(analyzed_seq.gravy()) # -0.55378 showing strong hydrophobic properties
count = 0
for p in seq:
    if p == 'A' or p == 'V' or p == 'L' or p == 'I' or p == 'P' or p == 'M' or p == 'F' or p == 'W':
        count += 1
print(count) # 92 hydrophobic AAs
print(count/len(seq)) # 36.65% hydrophobic proteins overall
print(analyzed_seq.secondary_structure_fraction()) # 28.69% helix, 23.11% turn, 22.31% sheet
