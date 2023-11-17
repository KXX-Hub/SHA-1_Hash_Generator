# SHA-1-Hash-Generator-CN

📖[English README.md](#SHA-1-Hash-Generator-EN)📖

## 這是一款用戶友好的應用程式，專為生成檔案的 SHA-1 哈希而設計，提供可靠且高效的方式來確保檔案完整性。

## 如何使用
- 下載 [最新Release](https://github.com/KXX-Hub/SHA-1_Hash_Generator/releases)。
- 填寫Config案所需的資訊。
- 執行 SHA-1_Hash_Generator.exe 以生成 SHA-1 Hash。
### 系統要求
- Python 3.6 或更高版本
### 關於config
```
# file_directory: 指定要進行哈希處理的檔案所在的目錄路徑。
# 如果未指明，預設為腳本當前所在的目錄。
file_directory : ''

# include_file: 要包含的檔案名稱列表，用 '&' 分隔。
# 只有列在這裡的檔案會進行哈希處理。
# 如果此處為空 ('')，則會處理目錄中的所有檔案。
include_file : ''

# exclude_file: 要排除的檔案名稱列表，用 '&' 分隔。
# 列在這裡的檔案將不進行哈希處理。
# 如果此處為空 ('')，則不排除任何檔案。
exclude_file : ''

# csv_file_directory: 輸出 CSV 檔案將被保存的目錄路徑。
# 如果未指明，預設為腳本當前所在的目錄。
csv_file_directory : ''

# csv_file_name: 輸出 CSV 檔案的名稱。
# 如果未指明，預設名稱將基於當前日期，後接 '_sha1'。
csv_file_name : ''
```
| 變數名稱              | 預設值                                             | 描述                                                         |
|----------------------|----------------------------------------------------|-------------------------------------------------------------|
| file_directory       | 腳本的當前目錄。                                   | 指定要進行哈希處理的檔案所在的目錄路徑。                     |
| include_file         | ''（空字串）                                       | 要包含的檔案名稱列表，用 '&' 分隔。只有列在這裡的檔案會進行哈希處理。如果此處為空，則會處理目錄中的所有檔案。 |
| exclude_file         | ''（空字串）                                       | 要排除的檔案名稱列表，用 '&' 分隔。列在這裡的檔案將不進行哈希處理。如果此處為空，則不排除任何檔案。         |
| csv_file_directory   | 腳本的當前目錄。                                   | 輸出 CSV 檔案將被保存的目錄路徑。                            |
| csv_file_name        | 基於當前日期，後接 '_sha1'。                        | 輸出 CSV 檔案的名稱。                                        |

## 貢獻專案

### 如何貢獻

1. Fork 此專案。
2. 將您 Fork 的專案克隆到您的本地機器。
3. 創建一個新的分支。
4. 貢獻您的代碼。
5. 提交/推送您的代碼。
6. 創建一個新的 Pull Request。
7. 等待回應。

### 代碼編寫/提交指南

* 保持每行代碼在 100 個字元以內。
* 變數和函數名稱使用 `snake_case` 命名方式。
* 在檔案末尾添加一個空白行。
* 優化代碼並移除不必要的導入。
* 使用以下格式撰寫提交訊息，並用英文書寫：
  * Update - 在此處寫入您的提交訊息
  * Fix bug - 在此處寫入您的提交訊息
  * Optimize - 在此處寫入您的提交訊息
  * Standardize - 在此處寫入您的提交訊息

### 建議/問題回報

如果您有任何建議或發現任何問題，請在 [Issue](https://github.com/KXX-Hub/SHA-1_Hash_Generator/issues) 提交您的反饋，我會盡快回應！


# SHA-1-Hash-Generator-EN
📖[繁體中文版README.md](#SHA-1-Hash-Generator-CN)📖

## This is a user-friendly application designed to generate SHA-1 hashes for files, providing a reliable and efficient way to ensure file integrity.

## How to use
- download the [latest release](https://github.com/KXX-Hub/SHA-1_Hash_Generator/releases)  .
- Fill the config file with the required information.
- Run SHA-1_Generator.exe to generate the SHA-1 hashes.
### Requirements
- Python 3.6 or higher versions
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
| Variable Name        | Default Value                                        | Description                                                  |
|----------------------|------------------------------------------------------|--------------------------------------------------------------|
| file_directory       | The current directory of the script.                 | The directory path of the files to be hashed.                |
| include_file         | '' (empty string)                                    | List of file names to include for hashing, separated by '&'. Only files listed here will be processed. If empty, all files in the directory will be processed. |
| exclude_file         | '' (empty string)                                    | List of file names to exclude from hashing, separated by '&'. Files listed here will not be processed. If empty, no files are excluded. |
| csv_file_directory   | The current directory of the script.                 | The directory path where the output CSV file will be saved.  |
| csv_file_name        | Based on the current date, followed by '_sha1'.      | The name of the output CSV file.                             |


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

