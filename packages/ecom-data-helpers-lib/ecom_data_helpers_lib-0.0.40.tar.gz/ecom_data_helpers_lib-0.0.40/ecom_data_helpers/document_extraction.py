from datetime import datetime
import time
from PyPDF2 import PdfReader
import pdf2image
from pdf2image import convert_from_path,convert_from_bytes
import docx
import json
import boto3
from typing import Union
from io import BytesIO
import httpx

# import pytesseract
from PIL import Image

from .exceptions import PdfImageExtractionExeception
from .utils import timeit

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\augusto.lorencatto\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

@timeit
def extract_text_from_image_using_textract(image : bytes) -> str:
    textract_client = boto3.client('textract')

    print("Interacting with AWS Textract...")
    response = textract_client.detect_document_text(
        Document={'Bytes': image}
    )

    extracted_text = ''.join([item['Text'] for item in response['Blocks'] if item['BlockType'] == 'LINE'])

    return extracted_text

def check_file_type(file_bytes: bytes) -> str:
    # Verifica se é um PDF
    if file_bytes.startswith(b'%PDF-'):
        return "pdf"
    
    # Verifica se é um DOCX (arquivos DOCX são ZIP)
    if file_bytes.startswith(b'PK\x03\x04'):
        return "docx"
    
    return "Unknown file type"

def extract_pdf_to_text(doc_bytes : bytes) -> Union[str,str]:

    pdf_stream = BytesIO(doc_bytes)
    reader = PdfReader(pdf_stream)

    conversion_process = "raw_pdf"
    
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    if len(text) < 100:

        # Raising exception
        # raise PdfImageExtractionExeception("Can't extract info from .pdf")

        conversion_process = "pdf_to_image"

        try:
            # Converting to image and using aws textract to extract text
            # images = convert_from_path(file_path,poppler_path="/opt/bin/") # OLD
            images = convert_from_bytes(
                doc_bytes,
                fmt=".jpeg",
                poppler_path=r"T:\libs\poppler\Library\bin"
            )
        except pdf2image.exceptions.PDFInfoNotInstalledError:
            images = convert_from_bytes(
                doc_bytes,
                fmt=".jpeg",
                poppler_path="/opt/bin/"
            )

        print(f"{len(images)} images generated from .pdf")

        for i,img in enumerate(images):

            #
            print(f"Processing image : {i}")

            #
            print("Saving tmp image...")
            img.save("/tmp/file.jpg","jpeg")

            #
            print("Opening tmp image...")
            f = open('/tmp/file.jpg','rb')

            #
            extracted_text : str = extract_text_from_image_using_textract(
                image=f.read()
            )

            text += extracted_text
    
    return text,conversion_process


def extract_docx_to_text(doc_bytes : bytes) -> str:
    stream = BytesIO(doc_bytes)

    doc = docx.Document(stream)

    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def doc_url_to_bytes(url) -> bytes:
    try:

        response = httpx.get(url,verify=False)

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to download image. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

