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
        :param file_type: 文档类型,默认为docx
        :param lang_from: 源语言,默认为zh
        :param lang_to: 目标语言,默认为en
        :return: 翻译任务的响应结果
        """
        if not url:
            raise ValueError("URL是必需的，且不能为空。")
        file_type = file_type or 'docx'
        lang_to = lang_to or 'zh'
        lang_from = lang_from or 'en'
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
        
        :param job_id: 翻译任务ID，通过文档翻译接口返回即翻译任务的唯一标识符且不能为空
        :return: 文档翻译结果
        """
        if not job_id:
            raise ValueError("Job是必需的，且不能为空。")
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
        
        :param text: 待检测的文本,不能为空
        :return: 检测结果
        """
        if not text:
            raise ValueError("Text是必需的，且不能为空。")
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
        
        :param text: 待翻译的文本，不能为空
        :param lang_from: 源语言,默认为auto
        :param lang_to: 目标语言,默认为en
        :param scene: 翻译场景,默认为common
        :return: 翻译结果
        """
        if not text:
            raise ValueError("Text是必需的，且不能为空。")
        lang_from =lang_from or 'auto'
        lang_to = lang_to  or 'zh'
        scene = "common"
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