from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import RunFileTranslationRequest, FileTranslationReq, RunGetFileTranslationResultRequest, \
    RunLanguageDetectionRequest, LanguageDetectionReq, RunTextTranslationRequest, TextTranslationReq

from .auth_config import get_nlp_client

class MTService:
    """
    机器翻译服务类，提供文本翻译和文档翻译功能。
    """
    def __init__(self):
        self.client = get_nlp_client()  # 初始化NLP客户端

    def file_translation(self, url, file_type, lang_from, lang_to):
        """
        文档翻译接口。
        
        :param url: 文档的URL
        :param file_type: 文档类型
        :param lang_from: 源语言
        :param lang_to: 目标语言
        :return: 翻译任务的响应结果
        """
        try:
            request = RunFileTranslationRequest()
            request.body = FileTranslationReq(
                type=file_type,
                to=lang_to,
                _from=lang_from,
                url=url
            )
            response = self.client.run_file_translation(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def get_file_translation_result(self, job_id):
        """
        获取文档翻译结果。
        
        :param job_id: 翻译任务ID
        :return: 文档翻译结果
        """
        try:
            request = RunGetFileTranslationResultRequest()
            request.job_id = job_id
            response = self.client.run_get_file_translation_result(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def language_detection(self, text):
        """
        语种检测接口。
        
        :param text: 待检测的文本
        :return: 检测结果
        """
        try:
            request = RunLanguageDetectionRequest()
            request.body = LanguageDetectionReq(
                text=text
            )
            response = self.client.run_language_detection(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def text_translation(self, text, lang_from, lang_to, scene="common"):
        """
        文本翻译接口。
        
        :param text: 待翻译的文本
        :param lang_from: 源语言
        :param lang_to: 目标语言
        :param scene: 翻译场景
        :return: 翻译结果
        """
        try:
            request = RunTextTranslationRequest()
            request.body = TextTranslationReq(
                scene=scene,
                to=lang_to,
                _from=lang_from,
                text=text
            )
            response = self.client.run_text_translation(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None


def print_error(e):
    """
    打印错误信息。

    :param e: 异常实例
    """
    for attr in ['status_code', 'request_id', 'error_code', 'error_msg']:
        value = getattr(e, attr)
        if value is not None:
            print(f"{attr}: {value}")