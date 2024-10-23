from  tiktoken import encoding_for_model
from enum import StrEnum
from tiktoken.model import MODEL_TO_ENCODING
import json

class TokeniserHelperExceptionErrors(StrEnum):
     UNSUPPORTED_MODEL = "Unsupported model {}."
     UNSUPPORTED_MODEL_CAPABILITIES = "Unsupported model capabilities {}."

class ModelMaximumRequestTokens:
    def __init__(self,input:int,output:int) -> None:
        self.input=input
        self.output=output
    def to_dict(self):
        return self.__dict__
class ModelCapabilities:
    def __init__(self,name:str,version:str,maximum_training_date:str,maximum_request_tokens:ModelMaximumRequestTokens) -> None:
        self.name=name
        self.version=version
        self.maximum_training_date=maximum_training_date
        if isinstance(maximum_request_tokens,ModelMaximumRequestTokens):
            self.maximum_request_tokens=maximum_request_tokens
        else:        
            self.maximum_request_tokens=ModelMaximumRequestTokens(**maximum_request_tokens)
    def to_dict(self):
        tmp = self.__dict__
        tmp["maximum_request_tokens"]=tmp["maximum_request_tokens"].to_dict()
        return tmp
class TokensWithModelCapabilitiesValidation:
    def __init__(self,num_tokens:int,validation_success:bool,remaining_tokens:int,maximum_request_tokens:ModelMaximumRequestTokens) -> None:
        self.num_tokens=num_tokens
        self.validation_success=validation_success
        self.remaining_tokens = remaining_tokens
        if isinstance(maximum_request_tokens,ModelMaximumRequestTokens):
            self.maximum_request_tokens=maximum_request_tokens
        else:        
            self.maximum_request_tokens=ModelMaximumRequestTokens(**maximum_request_tokens)
    def to_dict(self):
        tmp = self.__dict__
        tmp["maximum_request_tokens"]=tmp["maximum_request_tokens"].to_dict()
        return tmp
MODEL_CAPABILITIES = [
    ModelCapabilities(name="gpt-4o",version="2024-05-13",maximum_training_date="Oct 2023", maximum_request_tokens=ModelMaximumRequestTokens(input=128000,output=4096)).to_dict(),
    ModelCapabilities(name="gpt-4o",version="2024-08-06",maximum_training_date="Oct 2023",maximum_request_tokens=ModelMaximumRequestTokens(input=128000,output=16384)).to_dict(),
    ModelCapabilities(name="gpt-35-turbo",version="0125",maximum_training_date="Sep 2021",maximum_request_tokens=ModelMaximumRequestTokens(input=16385,output=4096)).to_dict(),
]

class TokeniserHelper:
    @classmethod
    def get_supported_models(cls):
        """
        Gets a dictionary of the models supported by their respective encodings.

        :return: A dictionary where the keys are the names of the models and the values ​​are their corresponding encodings.
        :rtype: dict[str, str]

        :example:
        ```python
        from tokeniser_helper import TokeniserHelper

        supported_models = TokeniserHelper.get_supported_models()
        for model, encoding in supported_models.items():
            print(f"tiktoken Model: {model}, Encoding scheme: {encoding}")
        # tiktoken Model: gpt-4o, Encoding scheme: o200k_base
        # tiktoken Model: gpt-35-turbo, Encoding scheme: cl100k_base
        ```
        ...
        """
        supported_models = {}
        for model, encoding in MODEL_TO_ENCODING.items():
            supported_models[model] = encoding
        return supported_models

    @classmethod
    def get_model_capabilities(cls, model: str = None, version: str = None) -> dict:
        """
        Retrieves the capabilities of a model based on its name and version.

        This function generates a dictionary with the capabilities of models loaded from `MODEL_CAPABILITIES`. 
        If a model name and version are specified, it returns the capabilities for that specific model and version.
        If no model name or version is specified, it returns a dictionary with all available model capabilities.

        Values taken from:
        https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models
        https://platform.openai.com/docs/models/gpt-4o

        :param model: The name of the model to search for. (optional)
        :param version: The version of the model to search for. (optional)
        :return: A dictionary containing:
            - The capabilities of the specified model if `model` and `version` are provided.
            - A dictionary with all model capabilities if `model` and `version` are not provided.
        :raises ValueError: If the specified model is not supported or not found in `MODEL_CAPABILITIES`.

        :example:
        ```python
        from tokeniser_helper import TokeniserHelper
        import json

        model_capabilities = TokeniserHelper.get_model_capabilities()
        print(json.dumps(model_capabilities,indent=4))

        model_capabilities = TokeniserHelper.get_model_capabilities("gpt-35-turbo","0125")
        print(json.dumps(model_capabilities,indent=4))
        ```
        """
        model_capabilities_json = {}
        format_name = "{}-{}"
        for item in MODEL_CAPABILITIES:
            model_capabilities = ModelCapabilities(**item)
            model_capabilities_json[format_name.format(model_capabilities.name, model_capabilities.version)] = model_capabilities.to_dict()
        if any([model is not None, version is not None]):
            response = model_capabilities_json.get(format_name.format(model, version))
            if response is None:
                raise ValueError(TokeniserHelperExceptionErrors.UNSUPPORTED_MODEL_CAPABILITIES.format(format_name.format(model, version)))
            else:
                return response
        else:
            return model_capabilities_json

    @classmethod
    def calculate_tokens(cls,message:str|dict, model: str = "gpt-3.5-turbo") -> int:
        """
        Counts the number of tokens in a given input, which can be a text string or a JSON object, using the specified model.

        :param message: The input data to count tokens for, which can be either a text string (str) or a JSON object (dict).
        :param model: The name of the model for which to count tokens. The default is "gpt-3.5-turbo".
        :return: The number of tokens in the input data.

        :raises ValueError: If the specified model is not supported.

        :example:
        ```python
        from tokeniser_helper import TokeniserHelper

        example01 = "Hello world ... !!!"
        num_tokens = TokeniserHelper.calculate_tokens(example01,"gpt-4o")
        print(f"num_tokens for example01 with model=gpt-4o: {num_tokens}")

        example02 = {
            "name"              : "Hello world program",
            "cwd"               : "/usr/bin/example",
            "supported_types"   : "srt,int,char"
        }
        num_tokens = TokeniserHelper.calculate_tokens(example02,"gpt-4o")
        print(f"num_tokens for example02 with model=gpt-4o: {num_tokens}")
        # num_tokens for example01 with model=gpt-4o: 6
        # num_tokens for example02 with model=gpt-4o: 26
        ```
        """
        try:
            if isinstance(message,dict):
                message=json.dumps(message)
            encoding = encoding_for_model(model)
            tokens = encoding.encode(message)
            return len(tokens)
        except KeyError:
            raise ValueError(TokeniserHelperExceptionErrors.UNSUPPORTED_MODEL.format(model))

    @classmethod
    def calculate_tokens_with_model_capabilities(cls,message:str|dict, model: str = "gpt-3.5-turbo", version: str = "0125") -> TokensWithModelCapabilitiesValidation:
        """
        Calculates the number of tokens in a given input and checks if it complies with the model's capabilities for the specified version.

        This function calculates the number of tokens required for a given message, compares it with the token limits of the specified model and version, 
        and returns an object indicating whether the message complies with the model's token limits.

        :param message: The input data to count tokens for, which can be either a text string (str) or a JSON object (dict).
        :param model: The name of the model to use for token calculation. The default is "gpt-3.5-turbo".
        :param version: The version of the model to use for validating token limits. The default is "0125".
        :return: An instance of `TokensWithModelCapabilitiesValidation` containing:
            - `num_tokens`: The number of tokens calculated for the input.
            - `validation_success`: A boolean indicating whether the number of tokens is within the model's limits.
            - `remaining_tokens`: The number of tokens remaining within the model's limit (positive value means within limits).
            - `maximum_request_tokens`: The maximum number of tokens allowed by the model for input.

        :raises ValueError: If the specified model or version is not supported or found in `MODEL_CAPABILITIES`.

        :example:
        ```python
        from tokeniser_helper import TokeniserHelper
        import json

        message = "Test message ... !!!" * 10000
        model_capabilities = TokeniserHelper.calculate_tokens_with_model_capabilities(message,"gpt-4o","2024-08-06")
        print(json.dumps(model_capabilities.to_dict(),indent=4))
        ```
        """
            
        num_tokens = cls.calculate_tokens(message,model)
        model_capabilities = ModelCapabilities(**cls.get_model_capabilities(model,version))
        validation_success = False
        remaining_tokens = model_capabilities.maximum_request_tokens.input - num_tokens
        if remaining_tokens > 0:
            validation_success = True
        return TokensWithModelCapabilitiesValidation(
            num_tokens=num_tokens,
            validation_success = validation_success,
            remaining_tokens = remaining_tokens,
            maximum_request_tokens=model_capabilities.maximum_request_tokens
        )
