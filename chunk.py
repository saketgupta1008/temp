import PyPDF2
import hashlib

# Function to generate hash ID for each chunk
def generate_hash_id(text_chunk):
    return hashlib.md5(text_chunk.encode('utf-8')).hexdigest()

# Function to read PDF and create chunks
def read_pdf_create_chunks(file_path, chunk_size=500):
    # Dictionary to store chunks with hash ID as key
    chunk_dict = {}

    # Open and read the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""

        # Extract text from each page
        for page in reader.pages:
            full_text += page.extract_text()

    # Split the text into chunks
    for i in range(0, len(full_text), chunk_size):
        chunk = full_text[i:i + chunk_size]
        
        # Generate a unique hash ID for each chunk
        hash_id = generate_hash_id(chunk)
        
        # Store the chunk in the dictionary
        chunk_dict[hash_id] = chunk

    return chunk_dict

# Path to your local PDF file
pdf_file_path = 'path/to/your/pdf_file.pdf'

# Create chunks and store in a dictionary
chunks_dict = read_pdf_create_chunks(pdf_file_path)

# Print the dictionary
for key, value in chunks_dict.items():
    print(f"Hash ID: {key}\nChunk: {value}\n")
