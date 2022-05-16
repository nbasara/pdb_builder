import sys
import requests
from Bio.PDB.PDBList import PDBList

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

def _get_file_IDs(file_path):
    """
    Given a file path open that file and read IDs and return as a list
    """
    with open(file_path, 'r') as fd:
        content = fd.read()
        protein_IDs = content.split()
        return protein_IDs

def _get_pdb(pdb_list, file_path):
    pdbl = PDBList()
    pdbl.download_pdb_files(pdb_list, file_format='pdb', pdir=file_path)
    '''
    commenting out for now awaiting clarification on how to gather this data
    if report:
        for protein in pdb_list:
            print(protein)
            structure = p.get_structure(protein,  file_path + 'pdb' + protein.lower() + '.ent')
            residues = structure.get_residues()
            count = 0 
            for residue in residues:
                count += 1
            print(count)
    '''

def main():
    """
    Download pdb files from source 
    """
    protein_ID = sys.argv[1]
    dest_path = sys.argv[2]
    # getting IDs from a file
    if '-f' in sys.argv:
        pdb_set  =  _get_file_IDs(protein_ID)
        _get_pdb(pdb_set, dest_path)
        return

    if '.' in protein_ID:
        pdb_set = _request_family(protein_ID)
        if len(pdb_set) == 0:
            print("got nothing back from cath_id")
            return
        _get_pdb(pdb_set, dest_path)
    else:
        _get_pdb([protein_ID], dest_path)


if __name__ ==  '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 protdb.py protien_name destination_path')
    main()
