import os

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

# Read contents of all files
file_contents = read_files(filenames)
print(file_contents)
