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

from collections import Counter

# List of common words to exclude
common_words = {"A", "AND", "AN", "OF", "IN", "THE"}

# Function to get top 15 frequent words, excluding common ones
def get_top_words(text, top_n=15):
    words = text.split()
    # Filter out common words
    filtered_words = [word for word in words if word not in common_words]
    # Count word frequencies
    word_counts = Counter(filtered_words)
    # Get top N frequent words
    top_words = word_counts.most_common(top_n)
    return top_words

# Apply to each cleaned content
top_words_per_file = {filename: get_top_words(content) for filename, content in cleaned_contents.items()}
print(top_words_per_file)
