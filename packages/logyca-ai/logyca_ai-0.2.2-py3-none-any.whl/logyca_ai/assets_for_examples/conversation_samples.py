from logyca_ai.utils.schemes.input.conversations import (
    AssistantMessage,
    Content,
    ImageFileMessage,
    MicrosoftFileMessage,
    PdfFileMessage,
    PlainTextFileMessage,
    UserMessage,
)
from logyca_ai.assets_for_examples.file_or_documents.image_base64 import image_base64_sample
from logyca_ai.assets_for_examples.file_or_documents.ms_excel_base64 import ms_excel_base64_sample
from logyca_ai.assets_for_examples.file_or_documents.ms_word_base64 import ms_word_base64_sample
from logyca_ai.assets_for_examples.file_or_documents.pdf_base64 import pdf_base64_sample
from logyca_ai.assets_for_examples.file_or_documents.plain_text_base64 import plain_text_base64
from logyca_ai.utils.constants.content import ContentType
from logyca_ai.utils.constants.image import ImageResolution
from logyca_ai.utils.helpers.content_loaders import load_text_from_url
import base64

URL_PNG="https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/image.png"
URL_PDF="https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/pdf.pdf"
URL_CSV="https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/plain_text.csv"
URL_DOCX="https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/ms_word.docx"
URL_XLSX="https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/ms_excel.xlsx"

def encode_str_base64(message: str) -> str:
    """
    Encodes a given message into Base64.

    :param message: The message to encode.
    :return: The encoded message in Base64.
    """
    try:
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Could not decode base64 string {e}")

def get_content_simple_sample()->Content:
    return Content(
        system="""
                    Voy a definirte tu personalidad, contexto y proposito.
                    Actua como un experto en venta de frutas.
                    Se muy positivo.
                    Trata a las personas de usted, nunca tutees sin importar como te escriban.
                """.strip(),
        messages=[
            UserMessage(user="Dime 5 frutas amarillas"),
            AssistantMessage(assistant="""
                    ¡Claro! Aquí te van 5 frutas amarillas:

                    1. Plátano
                    2. Piña
                    3. Mango
                    4. Melón
                    5. Papaya
                """
            ),
            UserMessage(user="Dame los nombres en ingles."),
        ]
        )

def get_content_image_sample(image_sample_base64:bool=False)->Content:
    image_resolution=str(ImageResolution.AUTO)
    if image_sample_base64:
        base64_content_or_url=image_base64_sample
        image_format="png"
        type_message=ContentType.IMAGE_BASE64
    else:
        base64_content_or_url=URL_PNG
        image_format=ContentType.IMAGE_URL
        type_message=ContentType.IMAGE_URL
    return Content(
        system="""
                Actua como una maquina lectora de imagenes.
                Devuelve la información sin lenguaje natural, sólo responde lo que se está solicitando.
                El dispositivo que va a interactuar contigo es una api, y necesita la información sin markdown u otros caracteres especiales.
                """.strip(),
        messages=[
            UserMessage(
                user="Extrae el texto que recibas en la imagen y devuelvelo en formato json.",
                type=type_message,
                additional_content=ImageFileMessage(
                    base64_content_or_url=base64_content_or_url,
                    image_format=image_format,
                    image_resolution=image_resolution,
                ).to_dict()
            )
        ]
    )

def get_content_pdf_sample(pdf_sample_base64:bool=False)->Content:
    if pdf_sample_base64:
        base64_content_or_url=pdf_base64_sample
        pdf_format="pdf"
        type_message=ContentType.PDF_BASE64
    else:
        base64_content_or_url=URL_PDF
        pdf_format=ContentType.PDF_URL
        type_message=ContentType.PDF_URL
    return Content(
        system="""
                No uses lenguaje natural para la respuesta.
                Dame la información que puedas extraer de la imagen en formato JSON.
                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.
                """.strip(),
        messages=[
            UserMessage(
                user="Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia.",
                type=type_message,
                additional_content=PdfFileMessage(
                    base64_content_or_url=base64_content_or_url,
                    pdf_format=pdf_format,
                ).to_dict()
            )
        ]
    )

def get_content_plain_text_sample(file_sample_base64:bool=False)->Content:
    if file_sample_base64:
        base64_content_or_url=plain_text_base64
        file_format="csv"
        type_message=ContentType.PLAIN_TEXT_BASE64
    else:
        base64_content_or_url=URL_CSV
        file_format=ContentType.PLAIN_TEXT_URL
        type_message=ContentType.PLAIN_TEXT_URL
    return Content(
        system="""
                No uses lenguaje natural para la respuesta.
                Dame la información que puedas extraer en formato JSON.
                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.
                Te voy a enviar un texto que representa información en formato csv.
                """.strip(),
        messages=[
            UserMessage(
                user="""
                Dame los siguientes datos de la primera fila del documento: Expediente, radicación, Fecha, Numero de registro, Vigencia.
                A partir de la fila 2 del documento, suma los valores de la columna Valores_A.
                A partir de la fila 2 del documento, Suma los valores de la columna Valores_B.
                """.strip(),
                type=type_message,
                additional_content=PlainTextFileMessage(
                    base64_content_or_url=base64_content_or_url,
                    file_format=file_format,
                ).to_dict()
            )
        ]
    )

def get_content_microsoft_sample(file_sample_base64:bool=False,extension_for_example:str="docx")->Content:
    if file_sample_base64:
        if extension_for_example == "docx":
            base64_content_or_url=ms_word_base64_sample
        elif extension_for_example == "xlsx":
            base64_content_or_url=ms_excel_base64_sample
        else:
            base64_content_or_url="No example available at this time."
        file_format=extension_for_example
        type_message=ContentType.MS_BASE64
    else:
        if extension_for_example == "docx":
            base64_content_or_url=URL_DOCX
        elif extension_for_example == "xlsx":
            base64_content_or_url=URL_XLSX
        else:
            base64_content_or_url="No example available at this time."
        file_format=ContentType.MS_URL
        type_message=ContentType.MS_URL
    return Content(
        system="""
                No uses lenguaje natural para la respuesta.
                Dame la información que puedas extraer de la imagen en formato JSON.
                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.
                """.strip(),
        messages=[
            UserMessage(
                user="Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia.",
                type=type_message,
                additional_content=MicrosoftFileMessage(
                    base64_content_or_url=base64_content_or_url,
                    file_format=file_format,
                ).to_dict()
            )
        ]
    )

