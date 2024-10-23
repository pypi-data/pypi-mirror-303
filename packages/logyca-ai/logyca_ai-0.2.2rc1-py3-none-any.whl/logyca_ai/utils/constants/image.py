from enum import StrEnum

class ImageResolution(StrEnum):
   LOW = "low"
   HIGH = "high"
   AUTO = "auto"
   @classmethod
   def to_dict(self) -> str:
       return {item.name: item.value for item in ImageResolution}
   @classmethod
   def content_list(self) -> str:
       return [item.value for item in ImageResolution]

