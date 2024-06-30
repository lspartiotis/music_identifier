import os
import subprocess
import argparse

def query_fingerprint_db(db_filename, query_file):
    command = ['python', 'audfprint/audfprint.py', 'match', '--dbase', db_filename, query_file]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

def main():
    parser = argparse.ArgumentParser(description="Query fingerprint database")
    parser.add_argument('query_file', type=str, help='Path to the query song file')
    args = parser.parse_args()
    
    db_filename = 'audfprint/my_fingerprint_db.pklz'
    query_fingerprint_db(db_filename, args.query_file)

if __name__ == "__main__":
    main()
