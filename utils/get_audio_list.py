'''
Given a base directory, walk through one species only folder and
prepare the audio list csv input for Waveman
'''

import argparse
import csv
import os
import sys

IGNORED_FOLDERS = ['.DS_Store']
FOLDERS_OF_INTEREST = ['Only one species', 'one species only']

CSV_HEADERS = ['ID', 'Species', 'Audiofile']

CSV_PATH = '/Users/joanneong/Desktop/audio_list.csv'

def parse_args():
    '''
    Parses input arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='absolute path to base directory containing folders with species calls', type=str)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return args

def write_row(csv_writer, species_id, species, wav_file, wav_files_path):
    curr_row = [species_id, species, wav_files_path + os.sep + wav_file]
    csv_writer.writerow(curr_row)

def main():
    args = parse_args()
    folders = os.listdir(args.dir)
    # all_species = filter(lambda folder: folder not in IGNORED_FOLDERS, folders)
    all_species = ['Myotis muricola', 'Myotis adversus']

    with open(CSV_PATH, 'w+') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(CSV_HEADERS)
 
        for species in all_species:
            species_id = ''.join([w[0] for w in species.split()]).upper()

            species_subfolders_path = args.dir + os.sep + species
            species_subfolders = os.listdir(species_subfolders_path)
            for species_subfolder in species_subfolders:
                if species_subfolder not in FOLDERS_OF_INTEREST:
                    continue

                wav_files_path = species_subfolders_path + os.sep + species_subfolder
                wav_files = filter(lambda wav_file: wav_file.endswith('.wav'), os.listdir(wav_files_path))

                [write_row(csv_writer, species_id + '-' + str(index), species, wav_file, wav_files_path) for index, wav_file in enumerate(wav_files)]

        csv_file.close()

main()
