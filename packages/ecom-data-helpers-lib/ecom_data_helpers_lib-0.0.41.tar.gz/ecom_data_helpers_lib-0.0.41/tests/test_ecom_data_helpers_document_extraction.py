import pytest
import unittest
import os
from moto import mock_aws
from unittest.mock import patch

from ecom_data_helpers.document_extraction import (
    extract_docx_to_text,
    extract_pdf_to_text,
    check_file_type,
    extract_text_from_image_using_textract
)

from ecom_data_helpers.exceptions import PdfImageExtractionExeception


class TestEcomDataHelpersDocumentExtraction(unittest.TestCase):

    def setUp(self):

        self.ROOT_DIR =  os.path.dirname(os.path.abspath(__file__))

    def test_extract_docx_to_text_with_sucess(self):

        filepath : str = self.ROOT_DIR + "/data/exemplo.docx"
        with open(filepath, 'rb') as file: 
            text : str = extract_docx_to_text(doc_bytes=file.read())

            assert len(text) > 100

    def test_extract_pdf_to_text_with_sucess(self):
        
        filepath : str = self.ROOT_DIR + "/data/exemplo.pdf"

        with open(filepath, 'rb') as file: 
            text,conversion_process = extract_pdf_to_text(doc_bytes=file.read())

            assert len(text) > 100
            assert conversion_process == 'raw_pdf'

    @mock_aws
    def test_extract_text_from_image_using_textract_with_success(self):
        # Arrange
        filepath = self.ROOT_DIR + "/data/exemplo-imagem.jpg"
        
        # Configurar o mock do Textract
        with patch('boto3.client') as mock_client:
            mock_textract = mock_client.return_value
            mock_textract.detect_document_text.return_value = {
                'Blocks': [
                    {'BlockType': 'LINE', 'Text': 'Texto de exemplo'},
                    {'BlockType': 'LINE', 'Text': 'extraído da imagem'}
                ]
            }
            
            # Act
            with open(filepath, 'rb') as file:
                file_bytes = file.read()
                extracted_text = extract_text_from_image_using_textract(image=file_bytes)
            
            # Assert
            assert isinstance(file_bytes, bytes)
            assert isinstance(extracted_text, str)
            assert "Texto de exemplo" in extracted_text
            assert "extraído da imagem" in extracted_text
            mock_textract.detect_document_text.assert_called_once()

    # COSTS
    # def test_extract_pdf_to_text_using_pdf_from_images_with_sucess(self):
        
    #     filepath : str = self.ROOT_DIR + "/data/exemplo_pdf_imagem.pdf"

    #     with open(filepath, 'rb') as file: 
    #         text,conversion_process = extract_pdf_to_text(doc_bytes=file.read())

    #         assert len(text) > 100
    #         assert conversion_process == 'pdf_to_image'
    
    # DEPRECATED
    # def test_extract_pdf_to_text_with_error(self):

    #     filepath : str = self.ROOT_DIR + "/data/exemplo_pdf_imagem.pdf"

    #     with open(filepath, 'rb') as file: 

    #         with pytest.raises(PdfImageExtractionExeception, match="Can't extract info from .pdf"):
    #             extract_pdf_to_text(doc_bytes=file.read())

    def test_check_file_type_pdf_with_sucess(self):

        # Arrange
        filepath : str = self.ROOT_DIR + "/data/exemplo.pdf"

        # Act
        with open(filepath, 'rb') as file: 
            file_type : str = check_file_type(file_bytes=file.read())

            # Assert
            assert file_type == 'pdf'

    def test_check_file_type_docx_with_sucess(self):

        # Arrange
        filepath : str = self.ROOT_DIR + "/data/exemplo.docx"

        # Act
        with open(filepath, 'rb') as file: 
            file_type : str = check_file_type(file_bytes=file.read())

            # Assert
            assert file_type == 'docx'

    # TODO : Faze sentido testar um serviço externo?
    # @mock_aws
    # def test_extract_text_from_image_using_textract_with_sucess(self):

    #     # Arrange
    #     filepath : str = self.ROOT_DIR + "/data/exemplo-imagem.jpg"

    #     # Act
    #     with open(filepath, 'rb') as file: 
            
    #         file_bytes : bytes = file.read()

    #         extracted_text : str = extract_text_from_image_using_textract(
    #             image=file_bytes
    #         )

    #         # print(extracted_text)

    #         # Assert
    #         assert type(file_bytes) == bytes
    #         assert type(extracted_text) == str


        




if __name__ == "__main__":
    unittest.main()