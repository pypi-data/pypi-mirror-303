[![Upload Python Package](https://github.com/JorgeCardona/git-history-analyzer/actions/workflows/python-publish.yml/badge.svg)](https://github.com/JorgeCardona/git-history-analyzer/actions/workflows/python-publish.yml)

# ⚠️☢️☣️ For this to work properly, it must be run within the main folder of a Git repository and Git must be installed. ☣️☢️⚠️
# Git History Analyzer

https://pypi.org/project/git-history-analyzer/

This package provides a simple way to analyze the commit history of a specified file in a Git repository. It retrieves the complete commit history along with the changes made in each commit, allowing users to track modifications effectively.

## Features

- Retrieve commit history for a specific file.
- Display details such as commit ID, author, date, and commit message.
- Track line changes with added and removed lines.

## Installation
You can install the package using pip:
```bash
pip install git-history-analyzer
```

## Usage

Here's how to use the `GitCommitsReportGenerator` function:

## Parameters

report_type=['blame', 'log_history'], print_details=False

- `list_files_to_read` (list): list of The path to the files you want to analyze. Please use single slashes (/) for linux or double backslashes (\\\\) for windows, depending on the operating system you are using to avoid directory-related issues.
- `report_type` (list) ['blame', 'log_history']
- `print_details` (bool): If set to `True`, the function will print the details of each commit. Default is `False`.

## Output

The function returns a list of dictionaries, where each dictionary contains:
- `Branch`: The branch currently under analysis.
- `commit_id`: The ID of the commit.
- `commit_author`: The author of the commit.
- `commit_email`: The author's email address.
- `commit_date`: The date of the commit.
- `commit_message`: The message associated with the commit.
- `changes`: A list of changes, each detailing the type (added or removed), the line content, and the line number.

# Reports Directory 
## for blame_report_main.py and log_history_main.py
<pre>
📦 jorge_cardona_project [project_directory]  
┗ report [package]  
┃ ┣ 📂 blame [package]  
┃ ┃ ┣ <span style="color: red;">blame_report_main.py</span>  
┃ ┣ 📂 log_history [package]  
┃ ┃ ┣ <span style="color: green;">log_history_main.py</span>  
┗ 📂 deployment [package]  
┗ 📂 requirements [package]  
┗ 📂 test [package]  
┗ 🐍 main.py [__main__]  
┗ 📜 README.md  
┗ ⚠️ .gitignore  
</pre>

## Example blame report
```python
from git_history_analyzer import GitCommitsReportGenerator

# Example usage
list_files_to_read = ['C:\\Users\\USUARIO\\Documents\\satellite_notifier\\main.py',
                      'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\.github\workflows\\main.yml']

GitCommitsReportGenerator(list_files_to_read=list_files_to_read,
                            report_type=['blame'],
                            print_details=True)
```

## Example Output - blame report
![blame](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/blame.png)

![git_blame_report](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/git_blame_report.png)

## Example log_history report
```python
from git_history_analyzer import GitCommitsReportGenerator

# Example usage
list_files_to_read = ['C:\\Users\\USUARIO\\Documents\\satellite_notifier\\main.py',
                      'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\.github\workflows\\main.yml']

GitCommitsReportGenerator(list_files_to_read=list_files_to_read,
                            report_type=['log_history'],
                            print_details=True)
```

## Example Output - log_history report
![log_history](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/log_history.png)

![git_log_history_report](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/git_log_history_report.png)

### Log History and Blame Reports (Without Print Details)
```python
from git_history_analyzer import GitCommitsReportGenerator

# Example usage
list_files_to_read = ['C:\\Users\\USUARIO\\Documents\\satellite_notifier\\main.py',
                      'C:\\Users\\USUARIO\\Documents\\satellite_notifier\\.github\workflows\\main.yml']

GitCommitsReportGenerator(list_files_to_read=list_files_to_read)
```

## Example Output - log_history report (Without Print Details)
![Alt text](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/blame_log_history.png)

![git_blame_report](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/git_blame_report.png)

![git_log_history_report](https://raw.githubusercontent.com/JorgeCardona/git-history-analyzer/refs/heads/main/images/git_log_history_report.png)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Project Link: [GitHub Repository](https://github.com/jorgecardona/git-history-analyzer)
