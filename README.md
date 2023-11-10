# SHA-1 Hash Generator
📖[English README.md](#SHA-1-Hash-Generator)📖

## This is a user-friendly application designed to generate SHA-1 hashes for files, providing a reliable and efficient way to ensure file integrity.

## How to use
- download the [latest release](https://github.com/KXX-Hub/SHA-1_Hash_Generator)  .
- Fill the config file with the required information.
- Run main.exe to generate the SHA-1 hashes.
### Requirements
- Python 3.6 or higher
### About Config
```
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
```

## Contributing to the Project

### How to Contribute

1. Fork this project.
2. Clone your forked project to your local machine.
3. Create a new branch.
4. Contribute your code.
5. Commit/Push your code.
6. Create a new Pull Request.
7. Wait for a response.

### Code Writing/Commit Guidelines

* Keep each line under 100 characters.
* Use `snake_case` for variable and function names.
* Add a trailing blank line at the end of files.
* Optimize code and remove unnecessary imports.
* Use the following format for commit messages and write them in English:
  * Update - your commit messages here
  * Fix bug - your commit messages here
  * Optimize - your commit messages here
  * Standardize - your commit messages here

### Suggestions/Issue Reporting

If you have any suggestions or discover any issues, please submit your feedback in the [Issues](https://github.com/KXX-Hub/SHA-1_Hash_Generator/issues) section, and I will respond as soon as possible!

