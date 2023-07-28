import sys
import argparse
import datetime
import subprocess
import json
import os
import platform
import hashlib
import time

def run_pmdump(pid, output_file):
    """
    Run pmdump on the specified process ID and save the output to the given file
    """
    try:
        subprocess.run(['./pmdump', f'+r+w+x+p', str(pid), output_file])
    except subprocess.CalledProcessError as e:
        print(f'Error running pmdump: {e}')

def extract_data_from_output_file(output_file):
    """
    Extract relevant data from the output file
    """
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
            return data
    except (IOError, json.JSONDecodeError) as e:
        print(f'Error extracting data from {output_file}: {e}')
        return None

def calculate_hash(file_path):
    """
    Calculate the hash value of a file
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            hash_value = hashlib.sha256(data).hexdigest()
            return hash_value
    except IOError as e:
        print(f'Error calculating hash: {e}')
        return None

def main():
    # Add your existing main function code here

    # Add a simple UI to display the information
    while True:
        print('Press "q" to quit')
        print('1. RAM Dump')
        print('2. Study Page File')
        choice = input('Enter your choice: ')

        if choice == '1':
            print('Initiating RAM Dump...')
            output_file = 'output_pmdump.bin'
            pid = '1928'  # Replace with the actual process ID
            run_pmdump(pid, output_file)

            if output_file:
                data = extract_data_from_output_file(output_file)
                if data:
                    # Display the extracted data
                    print(f"Data: {data}")
                    print("Press any key to continue or q to quit")
                    input('Continue: ')

                    # Calculate hash value
                    hash_value = calculate_hash(output_file)
                    if hash_value:
                        print(f"Hash Value: {hash_value}")
                    else:
                        print("Error calculating hash value")

        elif choice == '2':
            print('Studying Page File...')
            # Add code to study the page file

        elif choice.lower() == 'q':
            break

if __name__ == '__main__':
    main()
