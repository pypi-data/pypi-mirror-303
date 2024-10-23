"""
Functions to process PDFs
"""

from io import BytesIO  # type: ignore
from typing import Dict, List
from urllib.parse import urlparse

import requests
from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from PyPDF2 import PdfReader, PdfWriter

from autogs._static import (
    DEFAULT_ORC_PROCESSOR,
    DEFAULT_PROCESSOR_LOCATION,
    DEFAULT_PROJECT,
)


def _is_url(string):
    """
    Check if a string is a URL
    """
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def _get_processor_from_name(
    processor_name: str = DEFAULT_ORC_PROCESSOR,
    project_id: str = DEFAULT_PROJECT,
    location: str = DEFAULT_PROCESSOR_LOCATION,
):
    """
    Get a processor from its name
    """
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    parent = client.common_location_path(project_id, location)

    processor_list = client.list_processors(parent=parent)

    for processor in processor_list:
        if processor.display_name == processor_name:
            return processor
    return None


def get_pdf_content(file_path: str):
    """
    Get the content of a PDF file
    """
    if _is_url(file_path):
        response = requests.get(file_path)
        response.raise_for_status()  # Check if the request was successful
        return response.content
    else:
        # It's a local file path
        with open(file_path, "rb") as file:
            return file.read()


def _split_pdf(file_path: str, max_pages_per_chunk: int = 10):
    """
    Split a PDF file into chunks
    """
    file_content = get_pdf_content(file_path)
    input_pdf = PdfReader(BytesIO(file_content))
    pdf_chunks = []

    for i in range(0, len(input_pdf.pages), max_pages_per_chunk):
        pdf_writer = PdfWriter()
        for j in range(i, min(i + max_pages_per_chunk, len(input_pdf.pages))):
            pdf_writer.add_page(input_pdf.pages[j])

        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        pdf_chunks.append(output_stream.getvalue())

    return pdf_chunks


def process_single(
    file_content: bytes,
    processor_name: str = DEFAULT_ORC_PROCESSOR,
    project_id: str = DEFAULT_PROJECT,
    location: str = DEFAULT_PROCESSOR_LOCATION,
) -> dict:
    """
    Process a single PDF chunk
    Args:
        - file_content: Content of the PDF file
        - processor_name: Name of the processor
        - project_id: Google Cloud Project ID
        - location: Google Cloud Location

    Returns:
        A dictionary with the text and pages of the document
    """
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    processor = _get_processor_from_name(processor_name, project_id, location)

    raw_document = documentai.RawDocument(
        content=file_content,
        mime_type="application/pdf",
    )

    request = documentai.ProcessRequest(name=processor.name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    return {"text": document.text, "pages": document.pages}


def process_full(
    file_path: str,
    processor_name: str = DEFAULT_ORC_PROCESSOR,
    project_id: str = DEFAULT_PROJECT,
    location: str = DEFAULT_PROCESSOR_LOCATION,
) -> dict:
    """
    Process a full PDF file

    Args:
        - file_path: Path to the PDF file
        - processor_name: Name of the processor
        - project_id: Google Cloud Project ID
        - location: Google Cloud Location

    Returns:
        A dictionary with the text and pages of the document as lists
    """
    pdf_chunks = _split_pdf(file_path)
    results: Dict[str, List] = {"text": [], "pages": []}

    for pdf_chunk in pdf_chunks:
        _tmp = process_single(pdf_chunk, processor_name, project_id, location)
        results["text"].append(_tmp["text"])
        results["pages"].append(_tmp["pages"])

    return results


def get_string(
    file_path: str,
    processor_name: str = DEFAULT_ORC_PROCESSOR,
    project_id: str = DEFAULT_PROJECT,
    location: str = DEFAULT_PROCESSOR_LOCATION,
) -> str:
    """
    Get the text of a PDF file

    Args:
        - file_path: Path to the PDF file
        - processor_name: Name of the processor
        - project_id: Google Cloud Project ID
        - location: Google Cloud Location

    Returns:
        A string with the text of the document
    """
    processed = process_full(file_path, processor_name, project_id, location)
    return " ".join(processed["text"])


def get_string_list(
    file_path: str,
    processor_name: str = DEFAULT_ORC_PROCESSOR,
    project_id: str = DEFAULT_PROJECT,
    location: str = DEFAULT_PROCESSOR_LOCATION,
) -> str:
    """
    Get the text of a PDF file

    Args:
        - file_path: Path to the PDF file
        - processor_name: Name of the processor
        - project_id: Google Cloud Project ID
        - location: Google Cloud Location

    Returns:
        A list of strings with the text of the document
    """
    processed = process_full(file_path, processor_name, project_id, location)
    return processed["text"]
