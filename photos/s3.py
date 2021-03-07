import base64
import os
import uuid

import boto3
from botocore.config import Config
from botocore.exceptions import NoCredentialsError, ClientError
from rest_framework.exceptions import ValidationError

from gallery.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         config=Config(signature_version='s3v4'))


def save_to_s3(photo):
    head, data = photo.split(',', 1)
    f_ext = head.split(';')[0].split('/')[1]
    plain_data = base64.b64decode(data)
    content_type = f'image/{f_ext}'

    uid = uuid.uuid4()
    f_name = f"{uid}.{f_ext}"

    path = f'gallery/temp'
    os.mkdir(path)

    with open(f'{path}/{f_name}', 'wb') as f:
        f.write(plain_data)
    try:
        s3_client.put_object(Key=f'{f_name}', Body=plain_data, Bucket=AWS_STORAGE_BUCKET_NAME, ContentType=content_type)
        photo_url = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{f_name}'
        os.remove(f'{path}/{f_name}')
        os.rmdir(path)
    except (NoCredentialsError, ClientError):
        raise ValidationError('Sorry, was not possible to add this photo.')
    return photo_url
