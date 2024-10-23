from logyca_ai.utils.constants.content import ContentRole
from logyca_ai.utils.schemes.input.conversations import Content, ImageFileMessage, PdfFileMessage, PlainTextFileMessage, MicrosoftFileMessage
from logyca_ai.utils.schemes.output.conversations import ConversationAnswer, ConversationUsage
from openai import AsyncAzureOpenAI, AzureOpenAI
from openai.types.completion_usage import CompletionUsage
from starlette import status as http_status

class AzureOpenAIChatGPT():

    def __init__(self,azure_endpoint:str,api_key:str,api_version:str) -> None:
        self.async_client = AsyncAzureOpenAI(
            azure_endpoint=f"https://{azure_endpoint}.openai.azure.com",
            api_key=api_key,
            api_version=api_version
        )
        self.sync_client = AzureOpenAI(
            azure_endpoint=f"https://{azure_endpoint}.openai.azure.com",
            api_key=api_key,
            api_version=api_version
        )
    
    def build_conversation_message_list(self,content:Content,advanced_image_recognition:bool=False,ocr_engine_path:str=None,output_temp_dir:str=None,cleanup_output_temp_dir_after_hours: int = 24,just_extract_images:bool=False)->list:
        """
        Build the supported message list.

        :param content: Content to send to chatgpt, which consists of system and messages.
        :type content: str
        :param advanced_image_recognition: Indicates whether to perform text recognition on images within the files or documents.
                                If True, OCR techniques will be used to extract text from images.
        :type advanced_image_recognition: bool
        :param ocr_engine_path: Path to the OCR executable. If provided, this path will be used instead of the default.
        :type ocr_engine_path: str, optional
        :param output_temp_dir: Temporary directory for storing output files.
                                If not provided, a default tmp temporary directory in the application root folder will be used.
        :type output_temp_dir: str, optional
        :param cleanup_output_temp_dir_after_hours: Number of hours after which the files in the temporary directory will be deleted on the next call of the function.
        :type cleanup_output_temp_dir_after_hours: int, optional
        :param just_extract_images: Only return image list from document
        :type just_extract_images: bool, optional

        :return: Supported message list.
        :rtype: list

        :example:

        ## Example usage
        ```json
        {
            "system": "",
            messages=[
                    {"role":"system","content":""},
                    {"role":"user","content":""},
                    {"role":"assistant","content":""},
                    {"role":"user","content":""},
                    {"role":"assistant","content":""},
            ]
        }
        ```
        """

        messages= []

        if content.system and content.system!="":
            messages.append({"role":str(ContentRole.SYSTEM),"content":content.system})

        for message in content.messages:
            if isinstance(message,dict) is False:
                message=message.to_dict()
            assistant_message = message.get(ContentRole.ASSISTANT,None)
            if assistant_message is not None:
                messages.append({"role":str(ContentRole.ASSISTANT),"content":assistant_message})
            else:
                user_message = message.get(ContentRole.USER,None)
                if user_message is None:
                    raise ValueError(f"Unsupported role {user_message}")
                else:
                    type_message = message.get("type",None)                

                    if just_extract_images:
                        is_valid = False
                        just_extract_formats = PdfFileMessage.get_default_types() + MicrosoftFileMessage.get_default_types()
                        if type_message in just_extract_formats:
                            is_valid = True
                        if is_valid is False:
                            raise ValueError(f"just_extract_images is supported for the formats: {just_extract_formats}")

                    if type_message in ImageFileMessage.get_default_types():
                        additional_content = message.get("additional_content",None)
                        messages.append({"role":str(ContentRole.USER),"content":[
                            ImageFileMessage(**additional_content).build_message_content()
                        ]})

                    if type_message in PdfFileMessage.get_default_types():
                        additional_content = message.get("additional_content",None)
                        if just_extract_images:
                            return PdfFileMessage(**additional_content).build_message_content(just_extract_images=just_extract_images)
                        else:
                            messages.append({"role":str(ContentRole.USER),"content":
                                PdfFileMessage(**additional_content).build_message_content(advanced_image_recognition=advanced_image_recognition,ocr_engine_path=ocr_engine_path,output_temp_dir=output_temp_dir,cleanup_output_temp_dir_after_hours=cleanup_output_temp_dir_after_hours)
                            })

                    if type_message in PlainTextFileMessage.get_default_types():
                        additional_content = message.get("additional_content",None)
                        messages.append({"role":str(ContentRole.USER),"content":
                            PlainTextFileMessage(**additional_content).build_message_content()
                        })                        

                    if type_message in MicrosoftFileMessage.get_default_types():
                        additional_content = message.get("additional_content",None)
                        if just_extract_images:
                            return MicrosoftFileMessage(**additional_content).build_message_content(just_extract_images=just_extract_images)
                        else:
                            messages.append({"role":str(ContentRole.USER),"content":
                                MicrosoftFileMessage(**additional_content).build_message_content(advanced_image_recognition=advanced_image_recognition,ocr_engine_path=ocr_engine_path,output_temp_dir=output_temp_dir,cleanup_output_temp_dir_after_hours=cleanup_output_temp_dir_after_hours)
                            })                        

                    if user_message is not None and user_message!="":
                        messages.append({"role":str(ContentRole.USER),"content":user_message})


        return messages

    async def conversation_async(self,
        model:str,
        messages:list,
        limit_tokens_answer:int=4000,
        temperature:float=0.7,
        top_p:float=0.95)->tuple[int,ConversationAnswer]:
        """Description
        :return int,str: Http Status Code Response, Message
        
        References:

        - https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/migration
        
        """
        try:
            completion = await self.async_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature, # The closer you get to 1 the answer changes, if you want the same answer you should get closer to zero
                max_tokens=limit_tokens_answer,
                top_p=top_p, # 0.1 means only the tokens comprising the top 10% probability mass are considered. Default 1 => 100% probability mass are considered
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            response=completion.model_dump()
            usage:CompletionUsage = completion.usage
            conversation_response = ConversationAnswer()
            conversation_response.assistant = str(response['choices'][0]['message']['content']).strip()
            conversation_response.usage_data = ConversationUsage(**usage.__dict__)
            return http_status.HTTP_200_OK,conversation_response
        except Exception as e:
            return http_status.HTTP_429_TOO_MANY_REQUESTS,str(e)

    def conversation_sync(self,
        model:str,
        messages:list,
        limit_tokens_answer:int=4000,
        temperature:float=0.7,
        top_p:float=0.95)->tuple[int,ConversationAnswer]:
        """Description
        :return int,str: Http Status Code Response, Message
        
        References:

        - https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/migration
        
        """
        try:
            completion = self.sync_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature, # The closer you get to 1 the answer changes, if you want the same answer you should get closer to zero
                max_tokens=limit_tokens_answer,
                top_p=top_p, # 0.1 means only the tokens comprising the top 10% probability mass are considered. Default 1 => 100% probability mass are considered
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            response=completion.model_dump()
            usage:CompletionUsage = completion.usage
            conversation_response = ConversationAnswer()
            conversation_response.assistant = str(response['choices'][0]['message']['content']).strip()
            conversation_response.usage_data = ConversationUsage(**usage.__dict__)
            return http_status.HTTP_200_OK,conversation_response
        except Exception as e:
            return http_status.HTTP_429_TOO_MANY_REQUESTS,str(e)

