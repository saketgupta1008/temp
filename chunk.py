import PyPDF2
import hashlib
import nltk

# Download the NLTK punkt tokenizer for sentence splitting
nltk.download('punkt')

# Function to generate hash ID for each chunk
def generate_hash_id(text_chunk):
    return hashlib.md5(text_chunk.encode('utf-8')).hexdigest()

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

    # Tokenize the full text into sentences
    sentences = nltk.sent_tokenize(full_text)

    # Create chunks that end with the last complete sentence
    chunk = ""
    chunks = []
    for sentence in sentences:
        if len(chunk) + len(sentence) <= chunk_size:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = " ".join(sentences[sentences.index(sentence)-overlap_sentences:sentences.index(sentence)]) + " " + sentence + " "

    # Append the last chunk if it's not empty
    if chunk:
        chunks.append(chunk.strip())

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
