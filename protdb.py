import sys
import requests
from Bio.PDB.PDBList import PDBList

def _request_family(family_id):
    """
    arguement: family_id 
    return: list of pdb_codes - strings of len(4)
    """
    # make  request to cath rest_api
    # https://www.cathdb.info/version/v4_3_0/api/rest/superfamily/sfam_id/ec
    # parse json for pdb_codes first four char from domain_id
    # needs to be a set of the first four because multiple for different
    # possibilites
    # return set
    pass

def main():
    # determine type of protien_name given family_id or pdb_code
    # based on determination run code 
    # if flag given generate report
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(sys.argv[1], file_format='pdb', pdir=sys.argv[2])

if __name__ ==  '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 protdb.py protien_name destination_path')
    main()
