import os
import re

# List of filenames for easy iteration
filenames = ["textbook1.txt", "textbook2.txt", "textbook3.txt", "textbook4.txt", "textbook5.txt"]

# Function to read each file's content
def read_files(file_list):
    file_contents = {}
    for filename in file_list:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                file_contents[filename] = file.read()
        else:
            print(f"File {filename} not found.")
    return file_contents

# Function to clean and standardize text
def clean_text(text):
    # Convert to uppercase
    text = text.upper()
    # Remove non-alphanumeric characters (except spaces for word separation)
    text = re.sub(r'[^A-Z0-9\s]', '', text)
    return text

# Read contents of all files
file_contents = read_files(filenames)

# Apply cleaning function to each file's content
cleaned_contents = {filename: clean_text(content) for filename, content in file_contents.items()}
print(cleaned_contents)
