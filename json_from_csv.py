import csv
import json

# Function to read CSV and create JSON metadata
def create_json_from_csv(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the header row

        for row in reader:
            # Assuming the first column is the ID
            record_id = row[0]
            
            # Create a dictionary to hold the metadata
            metadata = {headers[i]: row[i] for i in range(len(headers))}
            
            # Define the JSON filename
            json_filename = f'audit_{record_id}.json'
            
            # Save the metadata to a JSON file
            with open(json_filename, mode='w') as json_file:
                json.dump(metadata, json_file, indent=4)
            print(f'Successfully created {json_filename}')

# Example usage
csv_file = 'stocks_sentiments.csv'  # Replace with your actual CSV file path
create_json_from_csv(csv_file)
