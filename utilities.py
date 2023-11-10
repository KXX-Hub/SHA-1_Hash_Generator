import os
import sys
from os.path import exists
import hashlib
import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | get_file_sha1_bot                |
# | Made by KXX (MIT License)        |
# ++--------------------------------++

# Configuration for the get_file_sha1_bot script

# file_directory: The directory path of the files to be hashed.
# If not specified, the default is the current directory of the script.
file_directory : ''

# include_file: A string of file names to include, separated by '&'.
# Only files listed here will be processed for hashing.
# If this is empty (''), all files in the directory are considered for processing.
include_file : ''

# exclude_file: A string of file names to exclude, separated by '&'.
# Files listed here will be skipped during hashing.
# If this is empty (''), no files are excluded from processing.
exclude_file : ''

# csv_file_directory: The directory path where the output CSV file will be saved.
# If not specified, the default is the current directory of the script.
csv_file_directory : ''

# csv_file_name: The name of the output CSV file.
# If not specified, the default name will be based on the current date followed by '_sha1'.
csv_file_name : ''

#-------------------------------------

"""
                )
    sys.exit()


def read_config():
    """Read the config file.
    Check if the config file exists, if not, create one.
    If it exists, read the config file and return the configuration as a dictionary.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, creating one by default.\nPlease finish filling config.yml")
        config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'csv_file_directory': data['csv_file_directory'],
                'csv_file_name': data['csv_file_name'],
                'include_file': data['include_file'],
                'exclude_file': data['exclude_file'],
                'file_directory': data['file_directory']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml. Please check if the file is correctly filled.\n"
            "If the problem can't be solved, consider deleting config.yml and restarting the program.\n")
        sys.exit()


def should_process_file(file, include_files, exclude_files):
    """Check if a file should be processed based on the include_files and exclude_files lists.
    :param file: The file name to check.
    :param include_files: A list of file names to include.
    :param exclude_files: A list of file names to exclude.
    :return: True if the file should be processed, False otherwise.
    """
    if include_files and file not in include_files:
        return False
    if exclude_files and file in exclude_files:
        return False
    return True


def calculate_sha1(file_path):
    """
    Calculate the SHA-1 hash of a file.
    :param file_path: The path to the file.
    :return: The SHA-1 hash of the file.
    """
    # Calculate the SHA-1 hash of a file
    sha1_hash = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read data in 64 KB blocks
            if not data:
                break
            sha1_hash.update(data)
    return sha1_hash.hexdigest()


def get_application_path():
    """
    Get the path of the application.
    It will return the path of the .exe file when compiled with PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        # The application is frozen
        return os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        return os.path.dirname(os.path.abspath(__file__))