# Pinecone Data Processing and Export Project

This project demonstrates the integration of Python with Pinecone for data processing, exporting results to Excel, CSV, and PDF, and handling Thai text with Thai font support. Below are the steps to set up and run the project.

---

## Prerequisites

Ensure the following tools and libraries are installed:

1. **Python**: Version 3.8 or higher.
2. **Pip**: Python package manager.
3. **Environment Variables**:
   - `PINECONE_API_KEY`: Your Pinecone API key.
   - `PINECONE_INDEX_NAME`: The name of your Pinecone index.
   - `NAMESPACE`: The namespace to query in Pinecone.
   - `PINECONE_ENVIRONMENT`: ENVIRONMENT index Pinecone.

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Install Dependencies

Use the `requirements.txt` file to install the necessary libraries:

```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX_NAME=your_index_name
NAMESPACE=your_namespace
PINECONE_ENVIRONMENT=your_environment
```

### 2. Place Thai Font File

Ensure the `THSarabunNew.ttf` file is placed in the root directory of the project.

---

## Usage

### 1. Retrieve Data from Pinecone and Export to Excel/CSV

Run the script to fetch data from Pinecone and export it to Excel and CSV files:

```bash
python retriever_xlsx_csv.py
```

This will generate the files `output.xlsx` and `output.csv` in the specified output path.

### 2. Retrieve Data from Pinecone and Export to PDF

Run the script to fetch data from Pinecone and export it to a PDF file:

```bash
python retriever_pdf.py
```

This will generate a PDF file (`output.pdf`) in the specified output path.

### 3. Upsert a PDF Document into Pinecone

To index a PDF document, place the file in the desired directory and run:

```bash
python upsert_pdf.py
```

This script will extract text from the PDF, normalize Thai text, and upload it to the specified Pinecone index.

---

## Key Scripts

1. **`retriever_xlsx_csv.py`**:
   - Fetches data from Pinecone and exports it to Excel and CSV files.

2. **`retriever_pdf.py`**:
   - Fetches data from Pinecone and exports it to a PDF file with Thai font support.

3. **`upsert_pdf.py`**:
   - Reads a PDF document, processes the text, and uploads it to Pinecone.

---
