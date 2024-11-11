import csv
import json
import os


"""
This script reads a CSV file and converts it to a JSON file.
"""

# Get current working directory
current_dir = os.getcwd()
print(current_dir)

# Set the file path
csv_file_path = os.path.join(current_dir, '.\src\input.csv') 

#convert csv to json
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Write the json data to a file
json_file_path = os.path.join(current_dir, '.\src\output.json') 
with open(json_file_path, 'w') as jsonfile:
    json.dump(data, jsonfile)
