import json

import pandas as pd

from finter.api.quanda_data_api import QuandaDataApi
from finter.settings import logger
from finter.framework_model import QuandaLoader

import io

class QuandaData:

    @staticmethod
    def help():
        help_str = \
"""
# get file type data
# in case of loading excel file, maybe you need install openpyxl package
# ex) pip install openpyxl
import pandas as pd
from io import BytesIO
data = QuandaData.get('object_name', is_file_type=True)
df = pd.read_excel(BytesIO(data))

# get json data
import pandas as pd
data = QuandaData.get('object_name')
df = pd.read_json(data)
"""
        logger.info(help_str)

    @staticmethod
    def object_list(prefix='', personal=False):
        try:
            data = QuandaLoader.get_object_list(
                object_type='path', object_value=prefix, personal=personal
            )
            return data
        except Exception as e:
            logger.error(f"API call failed: {e}")
            return []

    @staticmethod
    def get(object_name, is_file_type=False, personal=False):
        if is_file_type:
            # file_response = QuandaDataApi().quanda_data_get_file_retrieve(
            #     object_name=object_name,
            #     _preload_content=False
            # )
            response = QuandaDataApi().quanda_data_get_file_retrieve(
                object_name=object_name,
                personal=personal,
                _preload_content=False
            )

            # always use a chunked way
            preload_content = False

            if preload_content:
                # Read all content into memory
                content = response.read()
                return content
            else:
                # Return the response object for streaming

                # Usage example for loading into memory
                try:
                    # For large files, use streaming to load into memory

                    # Use BytesIO to accumulate the data in memory
                    memory_file = io.BytesIO()
                    chunk_size = 8192
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        memory_file.write(chunk)

                    # Get the full content as bytes
                    file_content = memory_file.getvalue()

                    logger.info(f"File loaded into memory. Content length: {len(file_content)} bytes")

                    # You can now use file_content as needed, for example:
                    # process_data(file_content)

                    # If you need to work with it as a file-like object again:
                    # memory_file.seek(0)  # Reset the position to the beginning
                    # Use memory_file for further processing if needed

                except Exception as e:
                    print(f"An error occurred: {e}")

                return file_content
        else:
            data = QuandaDataApi().quanda_data_get_retrieve(object_name=object_name, personal=personal)
            data = data['data']
        return data

    @staticmethod
    def put(data, key, personal=False):
        try:
            if not personal:
                raise Exception("Personal is required")

            if not isinstance(data, pd.DataFrame):
                raise Exception("Data should be pandas DataFrame")

            QuandaDataApi().quanda_data_create(
                data=data.to_json(), object_name=key, personal=personal
            )
        except Exception as e:
            logger.error(e)
            return None

    @staticmethod
    def upload_file(file, personal=False):
        try:
            if not personal:
                raise Exception("Personal is required")

            QuandaDataApi().quanda_data_upload_file_create(
                file_path=file,
                personal=personal
            )
        except Exception as e:
            logger.error(e)
            return None
