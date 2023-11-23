import re
from collections import defaultdict
from datetime import datetime

# Function to parse each entry
def parser(entry):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ([A-Z]+) (.+)'
    match = re.match(pattern, entry) 
    
    # Extracting the timestamp, level and message for each entry
    if match:
        timestamp_str, level, message = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        return timestamp, level, message
    else:
        return None

def main():
    log_file_path = 'C:/Users/ARZOO/OneDrive/Desktop/Assignment/system_log.txt' # Enter the file path of the system log file here 
    
    with open(log_file_path, 'r') as file:
        entries = file.readlines() # Grabs each entry from the file

    total_entries = 0
    level_count = defaultdict(int) # Stores counts of log entries for each level
    first_entry = defaultdict(lambda: None) # Stores the timestamp of the first entry for each level
    last_entry = defaultdict(lambda: None) # Stores the timestamp of the last entry for each level

    for entry in entries:
        total_entries += 1
        parsed_entry = parser(entry)
        if parsed_entry:
            timestamp, level, _ = parsed_entry

            # Update level count
            level_count[level] += 1

            # Update first entry timestamp if not set
            if first_entry[level] is None:
                first_entry[level] = timestamp

            # Always update last entry timestamp
            last_entry[level] = timestamp
        else:
             # Print a message for entries that failed to parse
            print(f"Failed to parse entry: {entry}")

     # Print the summary
    print("Total number of log entries:", total_entries)
    for level, count in level_count.items():
        print(f"{level} entries: {count}")
        print(f"\tFirst entry timestamp: {first_entry[level]}")
        print(f"\tLast entry timestamp: {last_entry[level]}")
        
if __name__ == "__main__":
    main()