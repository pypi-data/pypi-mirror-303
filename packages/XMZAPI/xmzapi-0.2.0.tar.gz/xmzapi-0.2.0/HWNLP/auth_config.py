import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdknlp.v2.region.nlp_region import NlpRegion
from huaweicloudsdknlp.v2 import NlpClient

# 填写您的AK和SK信息
ak = os.environ.get("huaweiak")
sk = os.environ.get("huaweisk")

def get_nlp_client():
    """
    获取配置好的NLP客户端实例。
    
    :return: 配置好的NlpClient实例
    """
    credentials = BasicCredentials(ak, sk)  # 创建认证信息实例
    config = HttpConfig.get_default_config()  # 获取默认的HTTP配置
    region = NlpRegion.value_of("cn-north-4")  # 设置服务区域
    client = NlpClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(region) \
        .build()
    return client