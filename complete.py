import os
import re

from collections import Counter

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

# Function to calculate similarity between two sets of top words
def calculate_similarity(words1, words2):
    # Extract words from the top N frequent pairs
    set1 = {word for word, _ in words1}
    set2 = {word for word, _ in words2}
    # Calculate intersection
    common_words = set1.intersection(set2)
    return len(common_words), common_words

# Find the most similar pair of files
similarity_scores = {}
files = list(top_words_per_file.keys())

for i in range(len(files)):
    for j in range(i + 1, len(files)):
        file1, file2 = files[i], files[j]
        score, common_words = calculate_similarity(top_words_per_file[file1], top_words_per_file[file2])
        similarity_scores[(file1, file2)] = (score, common_words)
        
# Find the pair with the highest similarity
most_similar_pair = max(similarity_scores, key=lambda pair: similarity_scores[pair][0])
most_similar_score, common_words = similarity_scores[most_similar_pair]

# Display results
print("Similarity scores between files:", similarity_scores)
print()
print(f"The most similar files are {most_similar_pair} with {most_similar_score} common words: {common_words}")
