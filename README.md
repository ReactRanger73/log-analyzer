# Log Analyzer Script

## Overview
This Python script analyzes log files and provides a summary of key information. It reads log entries from a file in the format:
[YYYY-MM-DD HH:MM:SS] [LEVEL] Message

The script will display the total number of log entries, counts for each log level (INFO, WARNING, ERROR), 
and timestamps for the first and last entries of each level.

## File Structure
- `log_analyzer.py`: The main Python script.
- `system.log`: Sample log file for testing.
- `README.md`: This file, providing instructions and information about the script.

## Notes
- Ensure that you have Python installed on your system.
- Modify the `log_file_path` variable in the script if your log file has a different name or path.


## Sample Output
Total number of log entries: 3
INFO entries: 1
First entry timestamp: 2023-07-15 14:12:33
Last entry timestamp: 2023-07-15 14:12:33

WARNING entries: 1
First entry timestamp: 2023-07-15 14:13:07
Last entry timestamp: 2023-07-15 14:13:07

ERROR entries: 1
First entry timestamp: 2023-07-15 14:14:15
Last entry timestamp: 2023-07-15 14:14:15



