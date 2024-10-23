import boto3

from finter.rest import ApiException
from finter.settings import get_api_client, logger
import finter


def get_aws_credentials(object_type, object_value, personal):
    api_instance = finter.AWSCredentialsApi(get_api_client())

    try:
        api_response = api_instance.aws_credentials_quanda_retrieve(
            object_type=object_type,
            object_value=object_value,
            personal=personal
        )
        return api_response
    except ApiException as e:
        print("Exception when calling AWSCredentialsApi->aws_credentials_quanda_retrieve: %s\n" % e)


def get_user_info():
    api_instance = finter.UserApi(get_api_client())
    user = api_instance.user_info_retrieve(item='id')
    return user


class QuandaLoader:
    bucket = 'quanda-data-production'

    @staticmethod
    def get_object_full_path(object_value, personal=False):
        if personal:
            user = get_user_info()
            return f"personal/{user.data}/{object_value}"
        return object_value

    @staticmethod
    def _get_s3_client(object_type, object_value, personal):
        credentials = get_aws_credentials(object_type, object_value, personal)
        return boto3.client(
                's3',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token
            )

    @classmethod
    def get_object_list(cls, object_type, object_value, personal=False):
        try:
            object_value = (object_value + "/").replace("//", "/")
            object_value = cls.get_object_full_path(object_value, personal)
            s3_client = cls._get_s3_client(object_type, object_value, personal)
            paginator = s3_client.get_paginator('list_objects_v2')

            response_iterator = paginator.paginate(
                Bucket=cls.bucket,
                Prefix=object_value
            )
            result = []
            for page in response_iterator:
                for content in page.get('Contents', []):
                    result.append(content['Key'])

            return result
        except Exception as e:
            raise Exception(f"QuandaLoader.get_object_list failed: {e}")
