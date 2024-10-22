import pytest
from readpdfs import ReadPDFs

def test_initialization():
    client = ReadPDFs(api_key="test_key")
    assert client.api_key == "test_key"
    assert client.base_url == "https://api.readpdfs.com"

# Add more tests as needed
