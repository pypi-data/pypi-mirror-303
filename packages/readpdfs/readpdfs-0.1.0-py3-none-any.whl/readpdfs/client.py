import requests
import json
from typing import Optional, Dict, Any, List

class ReadPDFs:
    def __init__(self, api_key: str, base_url: str = "https://backend.readpdfs.com"):
        self.api_key = api_key
        self.base_url = base_url

    def process_pdf(self, 
                    pdf_url: Optional[str] = None, 
                    file_path: Optional[str] = None, 
                    quality: str = "standard") -> Dict[str, Any]:
        """
        Process a PDF file and convert it to markdown.
        Args:
            pdf_url (str, optional): URL of the PDF file to process.
            file_path (str, optional): Path to a local PDF file to upload and process.
            quality (str, optional): Quality of processing, either "standard" or "high". Defaults to "standard".
        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/process_pdf/"
        headers = {
            "x-api-key": self.api_key,
        }
        
        if pdf_url and file_path:
            raise ValueError("Provide either pdf_url or file_path, not both.")
            
        if pdf_url:
            data = {
                "pdf_url": pdf_url,
                "quality": quality
            }
            response = requests.post(endpoint, headers=headers, json=data)
        elif file_path:
            with open(file_path, "rb") as file:
                files = {"file": file}
                data = {
                    "uploadFile": "true",
                    "quality": quality
                }
                response = requests.post(endpoint, headers=headers, data=data, files=files)
        else:
            raise ValueError("Either pdf_url or file_path must be provided.")
            
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def fetch_markdown(self, url: str) -> str:
        """
        Fetch the markdown content from a given URL.
        Args:
            url (str): URL of the markdown content.
        Returns:
            str: The markdown content.
        """
        endpoint = f"{self.base_url}/fetch_markdown/"
        params = {"url": url}
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def get_user_documents(self, clerk_id: str) -> List[Dict[str, Any]]:
        """
        Get a list of documents for a user.
        Args:
            clerk_id (str): The Clerk ID of the user.
        Returns:
            list: A list of dictionaries containing document information.
        """
        endpoint = f"{self.base_url}/user_documents/"
        params = {"clerk_id": clerk_id}
        headers = {
            "x-api-key": self.api_key,
        }
        
        response = requests.get(endpoint, params=params, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
