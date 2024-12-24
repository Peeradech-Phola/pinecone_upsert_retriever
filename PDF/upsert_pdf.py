import random
import fitz  # PyMuPDF
from pythainlp.util import normalize
from pinecone import Pinecone, ServerlessSpec, Index
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("PINECONE_API_KEY")
ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

if not API_KEY or not ENVIRONMENT:
    raise ValueError("API Key or Environment not set in .env file")

# Initialize Pinecone
pc = Pinecone(api_key=API_KEY)

# Create/check index
index_name = "test"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1024,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region=ENVIRONMENT)
    )

index_info = pc.describe_index(index_name)
index = Index(name=index_name, api_key=API_KEY, environment=ENVIRONMENT, host=index_info.host)

# Read PDF and combine all text using PyMuPDF
file_path = r"Path to PDF file"  ## Path to PDF file
filename = os.path.basename(file_path)

full_text = ""
pdf_document = fitz.open(file_path)
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    full_text += page.get_text()
pdf_document.close()

# Normalize Thai text to fix spacing and encoding issues
def normalize_thai_text(text):
    return normalize(text)

# Normalize the extracted text
normalized_text = normalize_thai_text(full_text)

# Create single vector for entire document
vector = [random.uniform(-1, 1) for _ in range(1024)]
metadata = {
    "text": normalized_text,  # ใช้ข้อความที่แก้ไขแล้ว
    "filename": filename
}

# Prepare the data for upsert
unique_id = f"doc_{filename}"

# Log before the upsert
print(f"Preparing to upsert document '{filename}' with ID '{unique_id}'...")

# Upload to Pinecone
index.upsert(vectors=[(unique_id, vector, metadata)])

# Log after the upsert
print(f"Document '{filename}' with ID '{unique_id}' uploaded successfully to Pinecone!")

# Optionally log the metadata to verify
print(f"Metadata for the document: {metadata}")
