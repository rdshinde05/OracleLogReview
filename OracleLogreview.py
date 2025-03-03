import re
import pandas as pd

# Function to read the log file and extract errors with account and connection info
def extract_errors_with_details(log_file_path):
    error_details = []
    connection_string = None
    
    with open(log_file_path, 'r') as file:
        for line in file:
            # Capture the connection string
            connection_match = re.search(r'Connection string = (.*)', line)
            if connection_match:
                connection_string = connection_match.group(1)

            # Capture the account and error message
            error_match = re.search(r'Create Account Request failed for account = (\w+). Error = (.*)', line)
            if error_match:
                account = error_match.group(1)
                error_message = error_match.group(2)
                # Append the extracted data to error details
                error_details.append((account, connection_string, error_message))

    return error_details

# Function to analyze the log and display errors in tabular format
def analyze_log(log_file_path):
    errors = extract_errors_with_details(log_file_path)
    
    if errors:
        # Convert the errors to a DataFrame for tabular display
        df = pd.DataFrame(errors, columns=['Account', 'Connection String', 'Error Message'])
        print("Error Log Analysis:")
        print(df)
    else:
        print("No errors found in the log file.")

# Provide the path to your log filell
log_file_path = '/pathtolog/oracle-nonProd.log'  # Change this to the actual log file path
analyze_log(log_file_path)
