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

def main():
    # determine type of protien_name given family_id or pdb_code
    # based on determination run code 
    # if flag given generate report
    pdb_set = _request_family(sys.argv[1])
    if len(pdb_set) == 0:
        print("got nothing back from cath_id")
    print(len(pdb_set))
    print(pdb_set)
    # pdbl = PDBList()
    # pdbl.retrieve_pdb_file(sys.argv[1], file_format='pdb', pdir=sys.argv[2])

if __name__ ==  '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 protdb.py protien_name destination_path')
    main()
