import sys
import requests
import pandas as pd
from Bio.PDB.PDBList import PDBList
from Bio.PDB.PDBParser import PDBParser 

def _request_family(family_id):
    """
    arguement: family_id 
    return: list of pdb_codes - strings of len(4)
    """
    s = f'https://www.cathdb.info/version/v4_3_0/api/rest/superfamily/{family_id}/ec'
    print(s)
    r = requests.get(url=s)
    data = r.json()
    pdb_codes = []
    for i in range(len(data['data'])):
        pdb_codes.append(data['data'][i]['domain_id'][:4])
    return list(set(pdb_codes))

def _get_pdb(pdb_list, file_path, report, csv_path):
    pdbl = PDBList()
    report_info = [] 
    column_names = ['name', 'type', 'cath_id', 'res_count']
    for protein in pdb_list:
        pdbl.retrieve_pdb_file(protein, file_format='pdb', pdir=file_path)
        if report:
            return
            
        

def main():
    protein_ID = sys.argv[1]
    dest_path = sys.argv[2]
    generate_report = False
    csv_path = ''
    if '-r' in sys.argv:
        generate_report = True 
        csv_path = sys.argv[sys.argv.index('-r') + 1]
    if '.' in: protein_ID:
        pdb_set = _request_family(protein_ID)
        if len(pdb_set) == 0:
            print("got nothing back from cath_id")
            return
        _get_pdb(pdb_set, dest_path, generate_report, csv_path)

if __name__ ==  '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 protdb.py protien_name destination_path')
    #main()
    pdbl = PDBList()
    pdbp = PDBParser()
    pdbl.retrieve_pdb_file(sys.argv[1], file_format='pdb', pdir=sys.argv[2])
    #pdbp.get


