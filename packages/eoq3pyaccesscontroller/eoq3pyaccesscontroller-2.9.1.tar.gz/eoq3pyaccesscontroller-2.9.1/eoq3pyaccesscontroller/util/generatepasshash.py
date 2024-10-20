'''
2022 Bjoern Annighoefer

'''

from passhash import GeneratePasshash

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pyaccesscontroller passhash generator')
    parser.add_argument('--pw', metavar='pw', type=str, default='DAMMMMN!#', help='the password', dest='pw')
    args = parser.parse_args()
    
    ph = GeneratePasshash(args.pw)
    
    print(ph)
    