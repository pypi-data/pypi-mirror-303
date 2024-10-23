from enum import StrEnum
import base64
import os
import requests

class ContentLoadersExceptionErrors(StrEnum):
    DECODING_ERROR = "Could not decode base64 string {}"
    DECODING_ERROR_COMMON_ENCODINGS = "Could not decode base64 string with common encodings {}"
    ERROR_DOWNLOADING_FILE = "Error downloading file {}"
    ERROR_LOADING_FILE_CONTENT = "Error loading file content {}"
    ERROR_SAVING_FILE = "Error saving file {}"

def get_base64_from_file(image_full_path):
    with open(image_full_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_base64_to_file(base64_string: str, output_folder: str, filename: str):
    binary_data = base64.b64decode(base64_string)
    output_path = os.path.join(output_folder, filename)
    with open(output_path, 'wb') as file:
        file.write(binary_data)

def save_file_from_url(url: str, output_folder: str, filename: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(ContentLoadersExceptionErrors.ERROR_DOWNLOADING_FILE.format(e))
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def load_text_from_url(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        return data
    except requests.exceptions.RequestException as e:
        raise RuntimeError(ContentLoadersExceptionErrors.ERROR_SAVING_FILE.format(e))
    except Exception as e:
        raise RuntimeError(ContentLoadersExceptionErrors.ERROR_LOADING_FILE_CONTENT.format(e))

def decode_base64_to_str(encoded_str: str) -> str:
    common_encodings = ['utf-8', 'iso-8859-1', 'latin-1', 'ascii', 'utf-16', 'utf-32']
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        for encoding in common_encodings:
            try:
                return decoded_bytes.decode(encoding)
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError(ContentLoadersExceptionErrors.DECODING_ERROR_COMMON_ENCODINGS.format(common_encodings))
    except Exception as e:
        raise ValueError(ContentLoadersExceptionErrors.DECODING_ERROR.format(e))