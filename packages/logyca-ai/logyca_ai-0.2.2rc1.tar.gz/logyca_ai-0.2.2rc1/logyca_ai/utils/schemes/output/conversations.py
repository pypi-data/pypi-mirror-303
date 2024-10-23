from pydantic import BaseModel, AliasChoices, Field, model_validator

class ConversationUsage(BaseModel):
    completion_tokens: int = Field(default=0,validation_alias=AliasChoices("completion_tokens"))
    prompt_tokens: int = Field(default=0,validation_alias=AliasChoices("prompt_tokens"))
    total_tokens: int = Field(default=0,validation_alias=AliasChoices("total_tokens"))
    
    @model_validator(mode="before")
    def check_keys(cls, values):
        return values

    def to_dict(self)->dict:
        return self.__dict__

class ConversationAnswer(BaseModel):
    assistant:str = Field(default="")
    usage_data:ConversationUsage = Field(default=ConversationUsage())

    def to_dict(self)->dict:
        tmp = self.__dict__.copy()
        tmp["usage_data"] = tmp["usage_data"].to_dict()
        return tmp

class ImageBase64(BaseModel):
    image_base64:str = Field(default="")
    image_format:str = Field(default="")

    def to_dict(self)->dict:
        return self.__dict__
