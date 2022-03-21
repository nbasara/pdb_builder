import sys
from Bio import SeqIO

def main():
    protein_ID = sys.argv[1]
    output_path = sys.argv[2]
    protein_path = 'pdb' + protein_ID + '.ent'
    for record in SeqIO.parse(protein_path, "pdb-seqres"):
        print()
        print(record.id, record.annotations['chain'])
        print(record.seq)
        print()

if __name__ == '__main__':
    main()
