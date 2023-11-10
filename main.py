import os
import csv
from datetime import datetime
import utilities as utils

# Use get_application_path() to set the base path for config and other resources
application_path = utils.get_application_path()

# Modify the path for reading the config file
config_file_path = os.path.join(application_path, 'config.yml')
config = utils.read_config()

csv_file_directory = config.get('csv_file_directory', application_path)
csv_file_name = config.get('csv_file_name', '')
include_file = config.get('include_file', '')
exclude_file = config.get('exclude_file', '')
file_directory = config.get('file_directory', application_path)

# Convert include and exclude file lists from string to list
include_files = include_file.split('&') if include_file else []
exclude_files = exclude_file.split('&') if exclude_file else []


def encrypt_file(directory):
    """
    Process files in a directory, calculate their SHA-1 hash, and write the results to a CSV file.

    :param directory: The directory to process files from.
    """
    date = datetime.now().strftime('%Y-%m-%d')
    output_directory = csv_file_directory if csv_file_directory else directory
    os.makedirs(output_directory, exist_ok=True)

    csv_filename = f'{csv_file_name}.csv' if csv_file_name else f'{date}_sha1.csv'
    csv_file = os.path.join(output_directory, csv_filename)

    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Path', 'SHA-1 Hash'])

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and utils.should_process_file(file, include_files, exclude_files):
                    sha1_hash = utils.calculate_sha1(file_path)
                    csv_writer.writerow([file_path, sha1_hash])
        print("CSV file created successfully.")
        print(f'CSV file directory: {output_directory}')
        print(f'CSV file name: {csv_filename}')


def process_file():
    """
    Main function to initiate file processing.
    """
    print("Welcome to the SHA-1 Hash Generator!")
    print("Please make sure that config.yml is filled correctly.\n"
          "If you are not sure, please delete config.yml and restart the program.\n")
    print("-------------------------------------")
    print("Processing files...")
    current_directory = file_directory if file_directory else application_path
    print(f'Files directory: {current_directory}')
    encrypt_file(current_directory)
    print('Successfully processed files')


if __name__ == "__main__":
    process_file()
    wait = input("Press enter to exit")