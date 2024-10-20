import subprocess
import re
from datetime import datetime
import os

class GitCommitsReportGenerator:

    def __init__(self, list_files_to_read, report_type=['blame', 'log_history'], print_details=False):
        """
        Initializes the report generation class and generates the specified reports.

        Parameters:
        list_files_to_read (list): A list of file paths for which reports will be generated.
        report_type (list): A list specifying the types of reports to generate. Defaults to ['blame', 'log_history'].
                            Possible values:
                            - 'blame': Generates a Git blame report for the files.
                            - 'log_history': Generates a log history report for the files.
        print_details (bool): If True, includes detailed output in the reports. Defaults to False.

        Attributes:
        - print_details (bool): Stores whether to include detailed output in the reports.
        - list_files_to_read (list): Stores the list of files to read for generating the reports.
        - report_type (list): Stores the types of reports to generate (blame, log history).
        - blame_directory_to_save_report (str): Directory path to save blame reports. Default is '/report/blame'.
        - blame_report_name_to_save (str): Default name for blame reports. Default is 'blame_report'.
        - history_directory_to_save_report (str): Directory path to save log history reports. Default is '/report/blame'.
        - history_report_name_to_save (str): Default name for log history reports. Default is 'blame_report'.

        The constructor also automatically calls `generate_commint_reports` to generate the specified reports 
        for the provided list of files.
        """
        
        self.print_details = print_details
        self.list_files_to_read = list_files_to_read
        self.report_type = report_type
        self.blame_directory_to_save_report = '/report/blame'
        self.blame_report_name_to_save = 'blame_report'
        self.history_directory_to_save_report = '/report/log_history'
        self.history_report_name_to_save = 'log_history'

        # Automatically generate reports based on the provided report type and list of files
        self.generate_commit_reports(report_type=self.report_type, list_files_to_read=self.list_files_to_read)


    def generate_report_name_and_report_directory(self, directory_to_save_report, report_name_to_save, file_to_read):
            """
            Generates the name and full directory path for saving an HTML report.

            Parameters:
            directory_to_save_report (str): The relative or absolute path to the directory where the report will be saved.
            report_name_to_save (str): The base name for the report file.
            file_to_read (str): The name of the file related to the report, which will be appended to the report name.

            Returns:
            tuple: A tuple containing:
                - report_name (str): The complete name of the report file, including the .html extension.
                - report_directory (str): The full path to the report file, including the directory and file name.
            """
            
            # Use os.path.join to handle paths correctly for Linux
            current_directory = os.getcwd()
            final_directory = current_directory.replace('\\', '/') + directory_to_save_report.replace('\\', '/')

            # Ensure file name is valid (replace any unwanted characters)
            file_to_read = file_to_read.replace(':', '_').replace('/', '_').replace('\\', '_')

            # Create the directory if it does not exist
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)

            # Construct report name
            report_name = f'{report_name_to_save}_{file_to_read}.html'

            # Full path to the report
            report_directory = os.path.join(final_directory, report_name)

            return report_name, report_directory

    def generate_commit_reports(self, report_type, list_files_to_read):
        """
        Generates either blame or log history reports for a list of files based on the specified report type.

        Parameters:
        report_type (str): Specifies the type of report to generate. Can be 'blame' for blame reports 
                        or 'log_history' for log history reports.
        list_files_to_read (list): A list of file paths for which the reports will be generated.

        This function iterates over the provided list of files and generates the appropriate report 
        based on the `report_type`. It calls `create_blame_report` if 'blame' is specified in the report type, 
        or `create_log_history_report` if 'log_history' is specified.

        The reports are generated with the details provided in the class attributes for report saving 
        paths and report names.
        """
        
        for file_to_read in list_files_to_read:

            if 'blame' in report_type:
                self.create_blame_report(
                    blame_file_to_read=file_to_read,
                    blame_print_details=self.print_details,
                    blame_directory_to_save_report=self.blame_directory_to_save_report,
                    blame_report_name_to_save=self.blame_report_name_to_save)

            if 'log_history' in report_type:
                self.create_log_history_report(
                    history_file_to_read=file_to_read,
                    history_print_details=self.print_details,
                    history_directory_to_save_report=self.history_directory_to_save_report,
                    history_report_name_to_save=self.history_report_name_to_save)

    def create_blame_report(self, 
                            blame_file_to_read,
                            blame_print_details,
                            blame_directory_to_save_report,
                            blame_report_name_to_save):
        """
        Creates a Git blame report and generates an HTML file based on the blame details.

        Parameters:
        blame_file_to_read (str): The path to the file for which the blame report is generated.
        blame_print_details (bool): If True, prints details about the blame for each commit.
        blame_directory_to_save_report (str): The directory where the HTML report will be saved.
        blame_report_name_to_save (str): The name of the HTML report file.

        This function retrieves the Git blame details for the specified file and generates 
        an HTML report with the information, saving it to the designated directory with the 
        specified report name.
        """
        self.blame_report_details  = self.git_blame_with_commit_details(blame_file_to_read=blame_file_to_read,
                                                                        blame_print_details=blame_print_details)
        
        self.generate_blame_html_report(blame_file_to_read=blame_file_to_read,
                                        blame_report_details=self.blame_report_details, 
                                        blame_directory_to_save_report=blame_directory_to_save_report,
                                        blame_report_name_to_save=blame_report_name_to_save
                                        )

    def create_log_history_report(self, 
                                history_file_to_read,
                                history_print_details,
                                history_directory_to_save_report,
                                history_report_name_to_save):
        """
        Creates a log history report and generates an HTML file based on the commit history details.

        Parameters:
        history_file_to_read (str): The path to the file for which the history report is generated.
        history_print_details (bool): If True, prints details about the commit history for each change.
        history_directory_to_save_report (str): The directory where the HTML report will be saved.
        history_report_name_to_save (str): The name of the HTML report file.

        This function retrieves the commit history details for the specified file and generates 
        an HTML report with the information, saving it to the designated directory with the 
        specified report name.
        """
        self.history_report_details  = self.git_history_with_line_changes(history_file_to_read=history_file_to_read,
                                                                        history_print_details=history_print_details)
        
        self.generate_html_report_history(history_file_to_read=history_file_to_read,
                                        history_report_details=self.history_report_details,
                                        history_directory_to_save_report=history_directory_to_save_report,
                                        history_report_name_to_save=history_report_name_to_save
                                        )

    def git_blame_with_commit_details(self, blame_file_to_read, blame_print_details=False):
        """
        Executes 'git blame' on the specified file and retrieves commit details for each line,
        including the current branch name. The line numbers reflect the current version of the file.
        
        Parameters:
        blame_file_to_read (str): The path to the file to analyze with 'git blame'.
        blame_print_details (bool): If True, prints the commit details for each line. Default is False.
        
        Returns:
        list: A list of dictionaries containing details for each line in the file, 
            with the current line numbers in the latest version.
        """
        details_list = []  # List to store details for each line

        # Get the current branch name
        branch_name = subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            text=True
        ).strip()

        # Execute git blame and retrieve all commit ids at once
        blame_output = subprocess.check_output(
            ['git', 'blame', '--line-porcelain', blame_file_to_read],
            text=True
        ).splitlines()

        # Read the current version of the file
        with open(blame_file_to_read, 'r', encoding='utf-8') as f:
            current_file_lines = f.readlines()

        current_commit = {}
        blame_line_index = 0

        for line in blame_output:
            if line.startswith('author '):
                current_commit['commit_author'] = line[7:].strip()
            elif line.startswith('author-mail '):
                # Remove angle brackets from the email address
                current_commit['commit_email'] = line[12:].strip('<>')
            elif line.startswith('author-time '):
                # Convert the author time (UNIX timestamp) to YYYY-MM-DD format
                timestamp = int(line[12:].strip())
                current_commit['commit_date'] = datetime.utcfromtimestamp(timestamp).strftime('%a %b %d %H:%M:%S %Y -0500')
            elif line.startswith('summary '):
                current_commit['commit_message'] = line[8:].strip()
            elif re.match(r'^[0-9a-f]{40} ', line):
                commit_id, line_number = line.split()[:2]
                current_commit['commit_id'] = commit_id
                current_commit['original_line_number'] = int(line_number)
            elif line.startswith('\t'):
                # This is the content line from git blame output
                current_commit['content_line'] = line[1:].strip()

                # Match this with the current file's line content and update the current line number
                if blame_line_index < len(current_file_lines):
                    current_commit['current_line_number'] = blame_line_index + 1
                    current_commit['current_content'] = current_file_lines[blame_line_index].strip()

                    # Ensure the content from git blame matches the current file content (if desired)
                    # if current_commit['content_line'] == current_commit['current_content']:
                    current_commit['branch_name'] = branch_name

                    # Asegurar que 'line_number' esté presente para evitar el KeyError
                    current_commit['line_number'] = current_commit.get('current_line_number', None)

                    details_list.append(current_commit.copy())

                    if blame_print_details:
                        print(
                            f"\033[1;36mBranch:\033[0m {current_commit['branch_name']} - "
                            f"\033[1;34mCurrent Line Number:\033[0m {current_commit['current_line_number']} - "
                            f"\033[1;32mCurrent Content:\033[0m {current_commit['current_content']}  - "
                            f"\033[0;33mCommit Message:\033[0m {current_commit['commit_message']} - "
                            f"\033[1;36mCommit Id:\033[0m {current_commit['commit_id']} - "
                            f"\033[1;35mAuthor:\033[0m {current_commit['commit_author']} - "
                            f"\033[1;31mEmail:\033[0m {current_commit['commit_email']} - "
                            f"\033[1;38;5;214mDate:\033[0m {current_commit['commit_date']}"
                        )
                    blame_line_index += 1

        return details_list  # Return the list of dictionaries

    def generate_blame_html_report(self, blame_report_details, blame_file_to_read, blame_directory_to_save_report='/report/blame', blame_report_name_to_save='blame_report'):
        """
        Generates an HTML report of Git blame details for a specified file.

        This function creates a styled HTML report containing a table with Git blame information, 
        including line numbers, content, commit IDs, commit messages, authors, emails, branch name, and commit dates.
        The report allows for filtering and sorting of the displayed data.

        Parameters:
        blame_report_details (list of dict): A list containing dictionaries with Git blame details for each line, 
                                        where each dictionary should include:
            - line_number (int): The line number in the file.
            - content_line (str): The content of the line.
            - commit_id (str): The ID of the commit.
            - commit_message (str): The message associated with the commit.
            - commit_author (str): The author of the commit.
            - commit_email (str): The email of the author.
            - commit_date (str): The date of the commit.
            - branch_name (str): The name of the branch.
        blame_file_to_read (str): The name of the file for which the Git blame report is generated.
        blame_directory_to_save_report (str, optional): The path to the directory where the report will be saved. Defaults to '/report/blame'.
        blame_report_name_to_save (str, optional): The base name for the report file. Defaults to 'blame_report'.

        Returns:
        None: The function saves the generated HTML report to the specified directory and prints a confirmation message.
        """

        # Sort the report details by line number in ascending order
        blame_report_details.sort(key=lambda x: int(x['line_number']))

        # Get the current branch name
        branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], text=True).strip()

        report_name, report_directory = self.generate_report_name_and_report_directory(blame_directory_to_save_report, blame_report_name_to_save, blame_file_to_read)

        # HTML table header with filters, sorting, and styling
        html_content = f"""
        <html>
        <head>
            <title>Git Blame Report for {blame_file_to_read}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                }}
                h1 {{
                    text-align: center;
                    color: #4a90e2;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                th, td {{
                    padding: 12px;
                    text-align: left;
                    border: 1px solid #ddd;
                }}
                th {{
                    background: linear-gradient(90deg, #4a90e2, #50c878);
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                    text-align: center;
                    position: relative;
                    border-top-left-radius: 6px;
                    border-top-right-radius: 6px;
                }}
                th:hover {{
                    background: linear-gradient(90deg, #50c878, #4a90e2);
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                tr:hover {{
                    background-color: #f1f1f1;
                }}
                .commit-id {{color: #1e90ff;}}
                .author {{color: #2e8b57;}}
                .email {{color: #ff6347;}}
                .date {{color: #ffa500;}}
                .content {{color: #4682b4;}}
                input {{
                    width: 95%;
                    padding: 8px;
                    margin: 8px 0;
                    box-sizing: border-box;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                }}
                th:after {{
                    content: " ⬍";
                    font-size: 14px;
                    color: white;
                    padding-left: 8px;
                }}
            </style>
            <script>
                // Function to filter the table
                function filterTable(columnIndex) {{
                    var input, filter, table, tr, td, i, txtValue;
                    input = document.getElementsByTagName("input")[columnIndex];
                    filter = input.value.toUpperCase();
                    table = document.getElementById("blameTable");
                    tr = table.getElementsByTagName("tr");
                    
                    for (i = 1; i < tr.length; i++) {{
                        td = tr[i].getElementsByTagName("td")[columnIndex];
                        if (td) {{
                            txtValue = td.textContent || td.innerText;
                            if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                                tr[i].style.display = "";
                            }} else {{
                                tr[i].style.display = "none";
                            }}
                        }}       
                    }}
                }}

                // Function to sort the table
                function sortTable(columnIndex) {{
                    var table, rows, switching, i, x, y, shouldSwitch, dir, switchCount = 0;
                    table = document.getElementById("blameTable");
                    switching = true;
                    dir = "asc"; // Set the sorting direction to ascending initially
                    
                    while (switching) {{
                        switching = false;
                        rows = table.rows;
                        
                        for (i = 1; i < (rows.length - 1); i++) {{
                            shouldSwitch = false;
                            x = rows[i].getElementsByTagName("td")[columnIndex];
                            y = rows[i + 1].getElementsByTagName("td")[columnIndex];
                            
                            if (dir == "asc") {{
                                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }} else if (dir == "desc") {{
                                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }}
                        }}
                        
                        if (shouldSwitch) {{
                            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                            switching = true;
                            switchCount++;
                        }} else {{
                            if (switchCount == 0 && dir == "asc") {{
                                dir = "desc";
                                switching = true;
                            }}
                        }}
                    }}
                }}
            </script>
        </head>
        <body>
            <h1>Git Blame Report for {blame_file_to_read}</h1>
            <h1>Branch : {branch_name}</h1>
            <table id="blameTable">
                <tr>
                    <th onclick="sortTable(0)">Branch<br><input type="text" onkeyup="filterTable(0)" placeholder="Filter by branch"></th>
                    <th onclick="sortTable(1)">Line Number<br><input type="text" onkeyup="filterTable(1)" placeholder="Filter by line number"></th>
                    <th onclick="sortTable(2)">Content<br><input type="text" onkeyup="filterTable(2)" placeholder="Filter by content"></th>
                    <th onclick="sortTable(3)">Commit ID<br><input type="text" onkeyup="filterTable(3)" placeholder="Filter by commit ID"></th>
                    <th onclick="sortTable(4)">Commit Message<br><input type="text" onkeyup="filterTable(4)" placeholder="Filter by commit message"></th>
                    <th onclick="sortTable(5)">Author<br><input type="text" onkeyup="filterTable(5)" placeholder="Filter by author"></th>
                    <th onclick="sortTable(6)">Email<br><input type="text" onkeyup="filterTable(6)" placeholder="Filter by email"></th>
                    <th onclick="sortTable(7)">Date<br><input type="text" onkeyup="filterTable(7)" placeholder="Filter by date"></th>
                </tr>
        """

        # Add rows to the HTML content based on the report details
        for detail in blame_report_details:
            html_content += f"""
                <tr>
                    <td>{branch_name}</td>
                    <td>{detail['line_number']}</td>
                    <td class="content">{detail['content_line']}</td>
                    <td class="commit-id">{detail['commit_id']}</td>
                    <td>{detail['commit_message']}</td>
                    <td class="author">{detail['commit_author']}</td>
                    <td class="email">{detail['commit_email']}</td>
                    <td class="date">{detail['commit_date']}</td>
                </tr>
            """

        # Close the HTML
        html_content += """
            </table>
        </body>
        </html>
        """

        # Save the HTML file with ISO-8859-1 encoding
        with open(report_directory, 'w', encoding='utf-16') as file:
            file.write(html_content)

        print(f"Styled GIT BLAME HTML report with sorting and filters generated: {report_directory}")

    def generate_html_report_history(self, history_report_details, history_file_to_read, history_directory_to_save_report='/report/log_history', history_report_name_to_save='history_report'):
        """
        Generates an HTML report based on the commit history details with column filters, sorting, and styled headers.

        Parameters:
        history_report_details (list): A list of dictionaries containing commit details and changes.
        history_file_to_read (str): The path to the file analyzed.
        history_report_name_to_save (str): The name of the output HTML file. Default is 'history_report.html'.
        """

        report_name, report_directory = self.generate_report_name_and_report_directory(history_directory_to_save_report, history_report_name_to_save, history_file_to_read)
        # HTML table header with filters, sorting, and styling
        # Get the current branch name
        branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], text=True).strip()
        
        html_content = f"""
        <html>
        <head>
            <title>Git History Report for {history_file_to_read}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                }}
                h1 {{
                    text-align: center;
                    color: #4a90e2;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                th, td {{
                    padding: 12px;
                    text-align: left;
                    border: 1px solid #ddd;
                }}
                th {{
                    background: linear-gradient(90deg, #4a90e2, #50c878);
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                    text-align: center;
                    position: relative;
                    border-top-left-radius: 6px;
                    border-top-right-radius: 6px;
                }}
                th:hover {{
                    background: linear-gradient(90deg, #50c878, #4a90e2);
                }}
                th::after {{
                    content: '\\25B2'; /* Arrow symbol for sorting */
                    font-size: 12px;
                    margin-left: 8px;
                    position: absolute;
                    right: 10px;
                }}
                th.sort-desc::after {{
                    content: '\\25BC'; /* Down arrow when sorted descending */
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                tr:hover {{
                    background-color: #f1f1f1;
                }}
                .commit-id {{color: #1e90ff;}}
                .author {{color: #2e8b57;}}
                .email {{color: #ff6347;}}
                .date {{color: #ffa500;}}
                .message {{color: #4682b4;}}
                .added {{color: #388e3c;}}  /* Darker green for additions */
                .removed {{color: #ff6347;}} /* Red for deletions */
                .branch {{color: #8b008b;}} /* Color for branch */
                input {{
                    width: 95%;
                    padding: 8px;
                    margin: 8px 0;
                    box-sizing: border-box;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                }}
            </style>
            <script>
                // Function to filter the table
                function filterTable(columnIndex) {{
                    var input, filter, table, tr, td, i, txtValue;
                    input = document.getElementsByTagName("input")[columnIndex];
                    filter = input.value.toUpperCase();
                    table = document.getElementById("historyTable");
                    tr = table.getElementsByTagName("tr");
                    
                    for (i = 1; i < tr.length; i++) {{
                        td = tr[i].getElementsByTagName("td")[columnIndex];
                        if (td) {{
                            txtValue = td.textContent || td.innerText;
                            if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                                tr[i].style.display = "";
                            }} else {{
                                tr[i].style.display = "none";
                            }}
                        }}       
                    }}
                }}

                // Function to sort the table
                function sortTable(columnIndex) {{
                    var table, rows, switching, i, x, y, shouldSwitch, dir, switchCount = 0;
                    table = document.getElementById("historyTable");
                    switching = true;
                    dir = "asc"; // Set the sorting direction to ascending initially
                    
                    while (switching) {{
                        switching = false;
                        rows = table.rows;
                        
                        for (i = 1; i < (rows.length - 1); i++) {{
                            shouldSwitch = false;
                            x = rows[i].getElementsByTagName("td")[columnIndex];
                            y = rows[i + 1].getElementsByTagName("td")[columnIndex];
                            
                            if (dir == "asc") {{
                                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }} else if (dir == "desc") {{
                                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }}
                        }}
                        
                        if (shouldSwitch) {{
                            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                            switching = true;
                            switchCount++;
                        }} else {{
                            if (switchCount == 0 && dir == "asc") {{
                                dir = "desc";
                                switching = true;
                            }}
                        }}
                    }}
                }}
            </script>
        </head>
        <body>
            <h1>Git History Report for {history_file_to_read}</h1>
            <h1>Branch : {branch_name}</h1>
            <table id="historyTable">
                <tr>
                    <th onclick="sortTable(0)">Branch<br><input type="text" onkeyup="filterTable(0)" placeholder="Filter by branch"></th>
                    <th onclick="sortTable(1)">Commit ID<br><input type="text" onkeyup="filterTable(1)" placeholder="Filter by commit ID"></th>
                    <th onclick="sortTable(2)">Author<br><input type="text" onkeyup="filterTable(2)" placeholder="Filter by author"></th>
                    <th onclick="sortTable(3)">Email<br><input type="text" onkeyup="filterTable(3)" placeholder="Filter by email"></th>
                    <th onclick="sortTable(4)">Date<br><input type="text" onkeyup="filterTable(4)" placeholder="Filter by date"></th>
                    <th onclick="sortTable(5)">Commit Message<br><input type="text" onkeyup="filterTable(5)" placeholder="Filter by commit message"></th>
                    <th onclick="sortTable(6)">Changes<br><input type="text" onkeyup="filterTable(6)" placeholder="Filter by changes"></th>
                </tr>
        """

        # Add rows to the HTML content based on the report details
        for commit in history_report_details:
            changes_html = ""
            for change in commit['changes']:
                line_style = "added" if change['type'] == 'added' else "removed"
                changes_html += f"<span class='{line_style}'>{'+' if change['type'] == 'added' else '-'} Line {change['line_number']}: {change['line']}</span><br>"

            html_content += f"""
                <tr>
                    <td class="branch">{commit.get('branch', 'Unknown')}</td>
                    <td class="commit-id">{commit['commit_id']}</td>
                    <td class="author">{commit.get('commit_author', 'Unknown')}</td>
                    <td class="email">{commit.get('commit_email', 'No email')}</td>
                    <td class="date">{commit.get('commit_date', 'Unknown')}</td>
                    <td class="message">{commit.get('commit_message', 'No message')}</td>
                    <td>{changes_html}</td>
                </tr>
            """
        
        # Close the HTML tags
        html_content += """
            </table>
        </body>
        </html>
        """
        
        # Save the HTML report to a file with utf-16 encoding
        with open(report_directory, 'w', encoding='utf-16') as file:
            file.write(html_content)

        print(f"GIT HISTORY HTML report generated: {history_report_name_to_save}")


    def git_history_with_line_changes(self, history_file_to_read, history_print_details=False):
        """
        Retrieves the complete commit history for a specified file along with the changes made in each commit, including branch names and real line numbers.

        Parameters:
        history_file_to_read (str): The path to the file to analyze.
        history_print_details (bool): If True, prints the changes for each commit. Default is True.

        Returns:
        list: A list of dictionaries containing details for each commit along with the changes.
        """
        history_list = []  # List to store details of each commit with line changes

        # Get the current branch
        branch_process = subprocess.Popen(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        current_branch, _ = branch_process.communicate()
        current_branch = current_branch.strip()  # Get branch name

        # Execute git log with patch to show changes
        process = subprocess.Popen(
            ['git', 'log', '-p', '--follow', '--', history_file_to_read],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Read the output line by line
        current_commit = None
        commit_details = {}
        current_line_number = 0
        current_hunk_new_start = None

        for line in process.stdout:
            line = line.rstrip()  # Remove trailing newline characters

            # Check for commit lines
            if line.startswith('commit '):
                if current_commit:  # If there is a current commit, save its details
                    history_list.append(commit_details)

                # Start a new commit details dictionary
                current_commit = line.split()[1]  # Extract commit ID
                commit_details = {'commit_id': current_commit, 'branch': current_branch, 'changes': []}

            elif line.startswith('Author:'):
                commit_details['commit_author'] = line[8:].strip()  # Extract author
                commit_details['commit_email'] = line.split('<')[1].strip('>')  # Extract email

            elif line.startswith('Date:'):
                commit_details['commit_date'] = line[8:].strip()  # Extract date

            elif line.startswith('    '):  # Lines starting with spaces are commit messages
                if 'commit_message' not in commit_details:  # Ensure to store commit message once
                    commit_details['commit_message'] = line.strip()  # Extract commit message

            elif line.startswith('@@'):
                # Extract line number from the hunk header (example: @@ -12,7 +12,7 @@)
                hunk_header = line.split(' ')
                new_hunk_info = hunk_header[2]  # This is the `+` section, representing the new file
                current_hunk_new_start = int(new_hunk_info.split(',')[0][1:])  # Get the starting line number of the new hunk

            elif line.startswith('+') and not line.startswith('+++'):
                # Lines starting with '+' are additions
                change_line = line[1:].strip()  # Remove the '+' sign
                commit_details['changes'].append({'type': 'added', 'line': change_line, 'line_number': current_hunk_new_start})
                current_hunk_new_start += 1  # Increment the line number for the next addition

            elif line.startswith('-') and not line.startswith('---'):
                # Lines starting with '-' are deletions (we keep track of the old line numbers similarly if needed)
                change_line = line[1:].strip()  # Remove the '-' sign
                commit_details['changes'].append({'type': 'removed', 'line': change_line, 'line_number': current_hunk_new_start})
                current_hunk_new_start += 1  # Increment the line number for the next removal

        # Add the last commit details if any
        if current_commit:
            history_list.append(commit_details)

        if history_print_details:
            for commit in history_list:
                print(f"\033[1;35mBranch:\033[0m {commit['branch']}")
                print(f"\033[1;36mCommit Id:\033[0m {commit['commit_id']}")
                print(f"\033[1;35mAuthor:\033[0m {commit.get('commit_author', 'Unknown')}")
                print(f"\033[1;31mEmail:\033[0m {commit.get('commit_email', 'No email')}")
                print(f"\033[1;38;5;214mDate:\033[0m {commit.get('commit_date', 'Unknown')}")
                print(f"\033[0;33mMessage:\033[0m {commit.get('commit_message', 'No message')}")
                print("\033[1;32mChanges:\033[0m")
                for change in commit['changes']:
                    print(f"  {'+' if change['type'] == 'added' else '-'} Line {change['line_number']}: {change['line']}")
                print()

        return history_list  # Return the list of commit details with line changes