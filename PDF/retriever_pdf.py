import os
import dotenv
from pinecone import Pinecone
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Load environment variables from .env file
dotenv.load_dotenv()

# Read environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Create Pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if the index exists
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    raise ValueError(f"Index '{PINECONE_INDEX_NAME}' does not exist.")

# Access the index
index = pc.Index(PINECONE_INDEX_NAME)

# Function to fetch data from Pinecone
def fetch_pinecone_data(top_k=20):
    dummy_vector = [0.0] * 1024  # Using dummy vector
    response = index.query(vector=dummy_vector, top_k=top_k, include_metadata=True)
    return response

# Fetch data
response = fetch_pinecone_data()
data = []
for match in response["matches"]:
    metadata = match.get("metadata", {})
    if metadata.get("filename") == "dummy filename here":  ## Dummy file name here
        text = metadata.get("text", "")
        print(metadata)

        # Split the text into parts and add them to the data list
        text_parts = text.split("\n")
        entry = ""
        for part in text_parts:
            if part.strip():
                entry += f"{part}<br/>"
        data.append(entry)

# Register Thai font
pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))

# Create PDF with Thai font support
output_file = r"Path Output/exaple.pdf"  ## Path Output
doc = SimpleDocTemplate(output_file, pagesize=letter)
elements = []

# Configure styles with Thai font
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='ThaiStyle',
                         fontName='THSarabunNew',
                         fontSize=14,
                         leading=16))
styles["Title"].fontName = 'THSarabunNew'
styles["Title"].fontSize = 16

# Add title to the document
title = Paragraph("Pinecone Data Export", styles["Title"])
elements.append(title)

# Add content from Pinecone data
if data:
    for entry in data:
        elements.append(Paragraph(entry, styles["ThaiStyle"]))
else:
    elements.append(Paragraph("No matching data found.", styles["ThaiStyle"]))

# Build the PDF
doc.build(elements)
print(f"Data saved to {output_file}")
