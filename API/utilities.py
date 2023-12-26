from sklearn.metrics.pairwise import cosine_similarity  # Import cosine_similarity for computing similarity between texts

from sklearn.feature_extraction.text import TfidfVectorizer  # Import TfidfVectorizer for text vectorization

# Define a function to calculate cosine similarity between two texts
def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()  # Initialize a TfidfVectorizer
    tfidf_matrix = vectorizer.fit_transform([text1, text2])  # Transform the texts into TF-IDF matrix
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]  # Return the cosine similarity score

# Define a function to load text lines from a file
def load(filename):
    lines = []  # Initialize an empty list to store lines
    with open(filename, 'r') as file:  # Open the file in read mode
        while True:
            line = file.readline()  # Read a line from the file
            if not line:  # Break the loop if no more lines
                break
            lines.append(line.strip())  # Add the line to the list after stripping whitespace
    return '\n'.join(lines)  # Return the lines joined by newlines
