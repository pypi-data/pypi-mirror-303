from enum import StrEnum
import os

class OCREngine(StrEnum):
    WINDOWS_PATH_01     = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    WINDOWS_PATH_02     = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    LINUX_PATH_01       = "/usr/bin/tesseract"
    LINUX_PATH_02       = "/usr/local/bin/tesseract"
    
    @classmethod
    def get_binary_path(cls):
        for location in cls:
            if os.path.exists(location):
                return str(location)
        return None

class OCREngineSettings(StrEnum):
    TMP_DIR="tmp"
