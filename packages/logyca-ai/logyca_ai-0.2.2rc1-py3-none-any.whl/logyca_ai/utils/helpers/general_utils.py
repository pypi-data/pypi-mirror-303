from datetime import datetime, timedelta
from urllib.parse import urlparse
import os
import random

def get_random_name_datetime():
    date_now = datetime.now()
    return "{}{}".format(date_now.strftime("%Y%m%d%H%M%S_"),random.randint(10000, 99999))

def delete_files_by_modification_hours(folder,hours_limit:int=8):
    now = datetime.now()
    time_limit = now - timedelta(hours=int(hours_limit))

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            modification_time = os.path.getmtime(file_path)
            modification_datetime = datetime.fromtimestamp(modification_time)
            if modification_datetime < time_limit:
                os.remove(file_path)

def get_file_name_extension_from_url(url: str) -> tuple[str,str]|None:
    """
    :return: file_name, file_extension or None,None if error.
    """
    try:
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        _, file_extension = os.path.splitext(file_name)
        return file_name, file_extension.split(".")[1]
    except:
        return None,None