# http://rosalind.info/problems/dna/

def counting_dna_nucleotides(dna_string):
    base_molecules_count = {'A': 0, 'C':0,
                            'G':0, 'T':0}

    for molecule in  dna_string:
        if molecule in base_molecules_count:
            base_molecules_count[molecule] += 1

    return base_molecules_count

def minimal_solution(dna_string):
    return dna_string.count('A'), dna_string.count('C'), dna_string.count('G'), dna_string.count('T')

def main():
    dna_string = 'AGCATGCTCTAAATCAGGTGATTCTACTATTCGGGCGACAATAGCGTGTGTTGTCTTCACGAACACATCTCGAATGCCTATATATTCAGGGCGACAAATGATTAGGCCAGGGGTACAAACTGGGTCAGAAAAGCCAGTACTTTCATGTCAACTGAATGTTAAGAGTGAGGTATGAAAATCAAACCCTACATATTTGCGGGAAGGCTGGTCTAAACAGTACCTGTACATCCCGCCCCCGAAGGGCCTTAGTCGATGTGACTTGGTCTTCGAATATAGCATTTTAGACTAAAAGTATGGTTACCTACACGTCGCCACTTAGATCTTTCCAGTTTTGAGGGGCATCCATATGAAAACTGTAGAGTGTATGTGCAAACTCGTCCTTTCCTGCAGCGGGTCAGGCGTTATAAGGCTATCCTGTAAGTTGAAAACATGGAAAGGACAGTCCACATTAGCGGTTTACCTTAACGTATGTAAGGAAATGTCAGAGGTACCTGGAATTGAGCAAAATAAGCGACACAACCCTGGACTCACCCGTTCTACTTTCTTTCTTTTTGACGATGAGTCTATTCCTAGGGAAGTCGGTAGACTATATGTGCATCGTACGCACTAAAGACAGCAAGGACTCTCCAAGCAGATACCTTCTAACCGATCAGGCGGCCAGGCAAACGACAGGTGTTTAGGGAAATGCTGTCACCCCCTGCTGTACGAAGGAGACTTGACCGGCGAATCCCCAAGTGTGGATTAACAATTAGACTACAAGTCAGCTCGGTGAGTTAGACCGCGTCAGCGTAGAGACAGTAGTGCGCGCAGCCACCAAAT'
    
    print(minimal_solution(dna_string))

if __name__ == '__main__':
    main()