import PyPDF2
import hashlib
import re

# Function to generate hash ID for each chunk
def generate_hash_id(text_chunk):
    return hashlib.md5(text_chunk.encode('utf-8')).hexdigest()

# Function to split text into sentences using regex
def split_into_sentences(text):
    # Regular expression to match sentence-ending punctuation
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    return sentence_endings.split(text)

# Function to read PDF, create chunks at sentence boundaries with overlap, and store them in a dictionary
def read_pdf_create_sentence_chunks(file_path, chunk_size=500, overlap_sentences=2):
    # Dictionary to store chunks with hash ID as key
    chunk_dict = {}

    # Open and read the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""

        # Extract text from each page
        for page in reader.pages:
            full_text += page.extract_text()

    # Split the text into sentences
    sentences = split_into_sentences(full_text)

    # Create chunks that end with the last complete sentence
    chunks = []
    chunk = ""
    i = 0
    while i < len(sentences):
        # Add sentences to chunk until it reaches the desired chunk size
        while i < len(sentences) and len(chunk) + len(sentences[i]) <= chunk_size:
            chunk += sentences[i] + " "
            i += 1

        # Add the chunk to the list of chunks
        chunks.append(chunk.strip())

        # Prepare the next chunk with overlapping sentences
        overlap_start = max(0, i - overlap_sentences)
        chunk = " ".join(sentences[overlap_start:i]) + " "

    # Create the dictionary with overlapping chunks
    for chunk in chunks:
        hash_id = generate_hash_id(chunk)
        chunk_dict[hash_id] = chunk

    return chunk_dict

# Path to your local PDF file
pdf_file_path = 'path/to/your/pdf_file.pdf'

# Create chunks with sentence boundaries and store in a dictionary
chunks_dict = read_pdf_create_sentence_chunks(pdf_file_path, chunk_size=500, overlap_sentences=2)

# Print the dictionary
for key, value in chunks_dict.items():
    print(f"Hash ID: {key}\nChunk: {value}\n")
