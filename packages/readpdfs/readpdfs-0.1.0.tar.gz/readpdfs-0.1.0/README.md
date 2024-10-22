# ReadPDFs

A Python client for the ReadPDFs API that allows you to process PDF files and convert them to markdown.

## Installation

```bash
pip install readpdfs
```

## Usage

```python
from readpdfs import ReadPDFs

# Initialize the client
client = ReadPDFs(api_key="your_api_key")

# Process a PDF from a URL
result = client.process_pdf(pdf_url="https://example.com/document.pdf")

# Process a local PDF file
result = client.process_pdf(file_path="path/to/local/document.pdf")

# Fetch markdown content
markdown = client.fetch_markdown(url="https://api.readpdfs.com/documents/123/markdown")

# Get user documents
documents = client.get_user_documents(clerk_id="user_123")
```

## Features

- Process PDFs from URLs or local files
- Convert PDFs to markdown
- Fetch markdown content
- Retrieve user documents
- Configurable processing quality

## Requirements

- Python 3.7+
- requests library

## License

This project is licensed under the MIT License - see the LICENSE file for details.
