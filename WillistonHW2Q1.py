# Download or copy-and-paste the DNA sequence of the Anthrax SASP gene from the
# anthrax_sasp.nuc file in the course data-directory. Treat the provided
# sequence as the sequence to be translated (no 5' UTR). Write a Python
# program to print answers to the following questions:
    # Does the SASP gene start with a Met codon?
    # Does the SASP gene have a frame 1 Met codon? 
    # How many nucleotides in the SASP gene?
    # How many amino-acids in the SASP protein?
    # What is the GC content (% G or C nucleotides) of the SASP gene?
# Test your program with other gene sequences.


# copied DNA sequence of Anthrax SASP gene
# AnthraxSASP = TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGC
#               TTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATG
#               GTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG

AnthraxSASP = 'TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'

# tested gene sequences
#AnthraxSASP = 'CAAAATAGGAGATGTGGAAAACCTGCCATGGGGTAGATTTAAGAGGCCTGATAATAG'
#AnthraxSASP = 'ATGCAAAATAGGAGATGTGGAAAACCTGCCATGGGGTAGATTTAAGAGGCCTGATAATAG'
#AnthraxSASP = 'ATG'
#AnthraxSASP = 'TAGCCCGTATCC'

# checking to see if the SASP gene starts with a Met codon
print('')
if AnthraxSASP.startswith('ATG'):
    print("Sequence starts with a Met codon")
else:
    print("Sequence does not start with a Met codon")
    

# checking to see if SASP gene has a frame 1 Met codon
PositionOfATG = AnthraxSASP.find('ATG')
TranslationFrame = (PositionOfATG) % 3 + 1

if TranslationFrame == 1:
    print(True,'. The Anthrax SASP gene has a frame 1 Met codon')
elif TranslationFrame == 2:
    print(False,'. The Anthrax SASP gene does not have a frame 1 Met codon')
elif TranslationFrame == 3:
    print(False, '. The Anthrax SASP gene does not have a frame 1 Met codon')
else:
    print(False,'The Anthrax SASP gene does not have a frame 1 Met codon')


# number of nucleotides in the SASP gene
NumOfANucs = AnthraxSASP.count('A')
NumOfCNucs = AnthraxSASP.count('C')
NumOfGNucs = AnthraxSASP.count('G')
NumOfTNucs = AnthraxSASP.count('T')
totalNucleotides = NumOfANucs + NumOfCNucs + NumOfGNucs + NumOfTNucs
print('Total Number of Nucleotides:', totalNucleotides)


# number of amino acids in the SASP protein
# divide sequence by 3's into amino acids
# remove any instances of stop codonds TAA, TAG, and TGA and/or start codons ATG
        # -- 5 instances of noncoding amino acids?
numAminoAcids = len(AnthraxSASP) // 3
print('Number of Amino Acids:',numAminoAcids)


# GC content of SASP gene
# GC content = [(G+C) / (A+T+G+C)]*100
GCcontent = ((NumOfGNucs + NumOfCNucs)/(totalNucleotides))*100
print('GC content:', GCcontent)
print('')

