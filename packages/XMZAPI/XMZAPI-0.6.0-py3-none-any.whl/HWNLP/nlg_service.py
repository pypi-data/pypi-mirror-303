from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import RunPoemRequest, CreatePoem, RunSummaryRequest, SummaryReq, RunSummaryDomainRequest, \
    SummaryDomainReq

from .auth_config import get_nlp_client

class NLGService:
    """
    自然语言生成服务类，提供诗歌生成和文本摘要功能。
    """
    def __init__(self):
        self.client = get_nlp_client()  # 初始化NLP客户端

    def poem(self, title, type, acrostic=False):
        """
        生成诗歌。
        
        :param title: 诗歌标题,不能为空
        :param type: 诗歌类型，默认为0
        :param acrostic: 是否为藏头诗，默认为false
        :return: 生成的诗歌内容
        """
        if not title:
            raise ValueError("title为必须参数")
        type = type or 0
        acrostic = acrostic or 'false'
        try:
            request = RunPoemRequest()
            request.body = CreatePoem(
                acrostic=acrostic,
                type=type,
                title=title
            )
            response = self.client.run_poem(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def summary(self, content, lang="zh", length_limit=0.3, title=None):
        """
        生成文本摘要。
        
        :param content: 原始文本内容,不能为空
        :param lang: 语言,默认为zh
        :param length_limit: 摘要长度限制,默认为0.3
        :param title: 文本标题,默认为0
        :return: 文本摘要内容
        """
        if not content:
            raise ValueError("content为必须参数")
        title = title or "0"
        lang = lang or "zh"
        length_limit = length_limit or 0.3
        try:
            request = RunSummaryRequest()
            request.body = SummaryReq(
                title=title,
                length_limit=length_limit,
                lang=lang,
                content=content
            )
            response = self.client.run_summary(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def summary_domain(self, content, lang="zh", length_limit=None, title=None, type=0):
        """
        生成领域特定文本摘要。
        
        :param content: 原始文本内容,不能为空
        :param lang: 语言,默认为zh
        :param length_limit: 摘要长度限制,默默认为0.3
        :param title: 文本标题,默认为0
        :param type: 领域类型,默认为0
        :return: 领域特定文本摘要内容
        """
        if not content:
            raise ValueError("content为必须参数")
        title = title or "0"
        lang = lang or "zh"
        length_limit = length_limit or 0.3
        try:
            request = RunSummaryDomainRequest()
            request.body = SummaryDomainReq(
                type=type,
                content=content,
                lang=lang,
                title=title,
                length_limit=length_limit
            )
            response = self.client.run_summary_domain(request)
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