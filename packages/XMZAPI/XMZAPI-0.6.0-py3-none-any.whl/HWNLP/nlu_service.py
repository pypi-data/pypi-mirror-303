from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import RunAspectSentimentRequest, AspectSentimentRequest, AspectSentimentAdvanceRequest, \
    RunAspectSentimentAdvanceRequest, RunClassificationRequest, ClassificationReq, RunDocClassificationRequest, \
    DocumentClassificationReq, RunDomainSentimentRequest, DomainSentimentReq, RunEntitySentimentRequest, \
    EntitySentimentReq, RunSemanticParserRequest, IntentReq, RunSentimentRequest, HWCloudSentimentReq

from .auth_config import get_nlp_client

class NLUService:
    """
    自然语言理解服务类，提供属性级情感分析、文本分类、意图识别等功能。
    """
    def __init__(self):
        self.client = get_nlp_client()  # 初始化NLP客户端

    def aspect_sentiment(self, content, type):
        """
        属性级情感分析接口。
        
        :param content: 待分析的文本内容
        :param type: 分析类型
        :return: 属性级情感分析结果
        """
        if None in content:
            raise ValueError("content是必须的参数")
        type = 1
        try:
            request = RunAspectSentimentRequest()
            request.body = AspectSentimentRequest(
                type=type,
                content=content
            )
            response = self.client.run_aspect_sentiment(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def aspect_sentiment_advance(self, content, type):
        """
        高级属性级情感分析接口。
        
        :param content: 待分析的文本内容,不能为零
        :param type: 分析类型，默认为1
        :return: 高级属性级情感分析结果
        """
        if None in content:
            raise ValueError("content是必须的参数")
        type = 1
        try:
            request = RunAspectSentimentAdvanceRequest()
            request.body = AspectSentimentAdvanceRequest(
                type=type,
                content=content
            )
            response = self.client.run_aspect_sentiment_advance(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def classification(self, content, domain=1):
        """
        文本分类接口。
        
        :param content: 待分类的文本内容,不能为零
        :param domain: 分类领域,默认为1
        :return: 文本分类结果
        """
        if not content:
            raise ValueError("content是必须的参数")
        domain = 1
        try:
            request = RunClassificationRequest()
            request.body = ClassificationReq(
                domain=domain,
                content=content
            )
            response = self.client.run_classification(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def doc_classification(self, content):
        """
        文档分类接口。
        
        :param content: 待分类的文档内容,不能为零
        :param lang: 语言,默认为zh
        :return: 文档分类结果
        """
        if not content:
            raise ValueError("content是必须的参数")
        lang = "zh"
        try:
            request = RunDocClassificationRequest()
            request.body = DocumentClassificationReq(
                lang=lang,
                content=content
            )
            response = self.client.run_doc_classification(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def domain_sentiment(self, content):
        """
        领域情感分析接口。
        
        :param content: 待分析的文本内容,不能为零
        :param type: 领域类型,默认为0
        :return: 领域情感分析结果
        """
        if not content:
            raise ValueError("content是必须的参数")
        type = 0
        try:
            request = RunDomainSentimentRequest()
            request.body = DomainSentimentReq(
                type=type,
                content=content
            )
            response = self.client.run_domain_sentiment(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def entity_sentiment(self, content, entity, type):
        """
        实体级情感分析接口。
        
        :param content: 待分析的文本内容,不能为零
        :param entity: 实体名称,不能为零
        :param type: 分析类型,默认为3
        :return: 实体级情感分析结果
        """
        if not content:
            raise ValueError("content是必须的参数")
        if not entity:
            raise ValueError("entity是必须的参数")
        type = 3
        try:
            request = RunEntitySentimentRequest()
            request.body = EntitySentimentReq(
                type=type,
                entity=entity,
                content=content
            )
            response = self.client.run_entity_sentiment(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def semantic_parser(self, text):
        """
        意图识别接口。
        
        :param text: 待识别的文本,不能为零
        :param lang: 语言,默认为zh
        :return: 意图识别结果
        """
        if not text:
            raise ValueError("text是必须的参数")
        lang = "zh"
        try:
            request = RunSemanticParserRequest()
            request.body = IntentReq(
                text=text,
                lang=lang
            )
            response = self.client.run_semantic_parser(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def sentiment(self, content):
        """
        情感分析接口。
        
        :param content: 待分析的文本内容,不能为零
        :param lang: 语言,默认为zh
        :return: 情感分析结果
        """
        if not content:
            raise ValueError("content是必须的参数")
        lang = "zh"
        try:
            request = RunSentimentRequest()
            request.body = HWCloudSentimentReq(
                lang=lang,
                content=content
            )
            response = self.client.run_sentiment(request)
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