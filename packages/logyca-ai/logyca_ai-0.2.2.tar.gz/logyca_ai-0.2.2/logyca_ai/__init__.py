from logyca_ai.assets_for_examples.conversation_samples import (
    get_content_image_sample,
    get_content_microsoft_sample,
    get_content_pdf_sample,
    get_content_plain_text_sample,
    get_content_simple_sample,
    )
from logyca_ai.utils.constants.content import ContentRole, ContentType
from logyca_ai.utils.constants.image import ImageResolution

from logyca_ai.utils.helpers.azure_openai_chatgpt import AzureOpenAIChatGPT
from logyca_ai.utils.helpers.content_loaders import (
    get_base64_from_file,
    load_text_from_url,
    save_base64_to_file,
    save_file_from_url,
)
from logyca_ai.utils.helpers.garbage_collector_helper import garbage_collector_at_the_end
from logyca_ai.utils.helpers.general_utils import get_random_name_datetime, delete_files_by_modification_hours, get_file_name_extension_from_url
from logyca_ai.utils.helpers.text_extraction_microsoft import extract_text_from_docx_file, extract_text_from_excel_file, extract_images_excel_file, extract_images_from_docx_file
from logyca_ai.utils.helpers.text_extraction_pdf import extract_text_from_pdf_file, extract_images_from_pdf_file
from logyca_ai.utils.helpers.tokeniser_helper import (
    MODEL_CAPABILITIES,
    ModelCapabilities,
    ModelMaximumRequestTokens,
    TokeniserHelper,
    TokeniserHelperExceptionErrors,
    TokensWithModelCapabilitiesValidation,
)

from logyca_ai.utils.schemes.input.conversations import (
    AssistantMessage,
    Content,
    ImageFileMessage,
    MicrosoftFileMessage,
    PdfFileMessage,
    PlainTextFileMessage,
    UserMessage,
    )
from logyca_ai.utils.schemes.output.conversations import ImageBase64