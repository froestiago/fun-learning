# http://rosalind.info/problems/revc/

from typing import Collection


def dna_complement(dna_string):
    dna_complement = ''
    for molecule in dna_string:
        if molecule == 'G':
            # dna_complement.append('C')
            dna_complement += 'C'
        if molecule == 'C':
            # dna_complement.append('G')
            dna_complement += 'G'
        if molecule == 'T':
            # dna_complement.append('A')
            dna_complement += 'A'
        if molecule == 'A':
            # dna_complement.append('T')
            dna_complement += 'T'
    return dna_complement[::-1]

def cool_solution(dna_string):
    dna_string = dna_string.replace('G', 'c').replace('C', 'g').replace('A', 't').replace('T', 'a').upper()[::-1]
    return dna_string

def using_dict(dna_string):     #I was thinking about something like this at first
    complement_dict = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    complement = ''
    # complement = []
    for molecule in dna_string[::-1]: 
        # complement.append(complement_dict[molecule])
        complement += complement_dict[molecule]
    # complement = ''.join(complement) #if using complement as a list. faster?
    return complement 
        


def main():
    dna_string = 'CATCATGTCCCACGCGCACGGGACGGGGGATCGATTCATCCGCCTCTGCAGAGTTGATGACTCGGCTGGACGCGTATTGTTGAATACCGTTTATAATTAGCCGCCCTTGTTGCTAAGTTATCCCGTCTCGATATTCCGTTGGATGAGTAGTAGTCTAGCGTAGCTACGGCTTATGTATGAGGGTGGACGCTCTAGCGGCATTGACGTACGCCTTTCAGGTCCTAACTCCCTTGAGCGGGTCGGCGCACGTTCCACCATCGGGCAGCCTTCGAACCTTATAGCTATGCCCAAGAGGTCCGAGGCCCATTCATACTCCCGCGTTGGCGGGGGGTCTGTTCGCGAACGTCAAATAGCCGATCTGTATGCGTCTAGTCGAGTGGTTTTAGAGCAGTGACGGCACAAGTCGTCGGTTCCGAAGCAAAGCGCTGCGATATTTCTCTGTCGGCGAAGTCCCATTCCAATCCTCAGGAGTCTGCATTCGACCAGATTAACGGGCGCTGCGGATGTCACTGTCCAGATCAACAACAAACTTTTATTTAATGCGGAGCCTCGACAGAAGGACATTAGCAGGACGTCCGGTCTCCTCTAAATTTACGGACGTTAAGCCTAATCGTGTCTGGAACACTTTACGGGGAACTTAATATTGTTTAAGCGCGAGCGGCTAGAGGTGAAGACAATGGGTATGGCCGCTGGAAGAATGCGAAAGCGTCCATACCCATCGGCATTCCTTCCATACATGTCTGGCCATTAAATACTTGATCGTCCTTAGAGTAGCAAAACAGACCAGCCCCAGGGGGTGCAAACCTTTTGCTCTGTCGGCGTTGCATAAGCTCCAAGCTGTCTTATTTGCGGAGACCAATTAAAGGAGGCTTCTTTTTCTACATTTGGCATATTTTACTGCGGCCATGGAATTCACATTGGTTCACCA'
    dna_string = 'AAAACCCGGT'
    print(dna_complement(dna_string))
    print(cool_solution(dna_string))
    print(using_dict(dna_string))

if __name__ == '__main__':
    main()