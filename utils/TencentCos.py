from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import json

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

app_id = '1258628713'
secret_id = 'AKIDwuPhjur2EAc08oMpOhkphKVO2Qedi2rS'
secret_key = 'VkkU4e0MgmPmshFcmmcbJkunjkU0EG9S'
region = 'ap-beijing'
proxies = {
    'http': '127.0.0.1:8080'
}
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Proxies=proxies)
client = CosS3Client(config)


def uploadImg(file_name, file_path, bucket='website-1258628713'):
    response = client.put_object(
        Bucket=bucket,
        Body=file_path,
        Key=file_name
    )
    print(response)
    return "https://{0}.cos.{1}.myqcloud.com/{2}".format(bucket, region, file_name)
