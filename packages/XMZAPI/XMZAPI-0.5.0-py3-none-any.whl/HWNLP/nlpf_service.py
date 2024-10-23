from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import RunDependencyParserRequest, DependencyParserRequest, RunEntityLinkingRequest, \
    PostEntityLinkingRequest, RunEventExtractionRequest, PostEventExtractionReq, RunKeywordExtractRequest, \
    KeywordExtractReq, RunMultiGrainedSegmentRequest, PostMultiGrainedSegmentReq, RunNerRequest, NerRequest, \
    RunNerDomainRequest, PostDomainNerRequest, RunSegmentRequest, SegmentRequest, RunSentenceEmbeddingRequest, \
    PostSentenceEmbeddingReq, RunTextSimilarityRequest, TextSimilarityRequest, RunTextSimilarityAdvanceRequest, \
    TextSimilarityAdvanceRequest

from .auth_config import get_nlp_client

class NLPFService:
    """
    自然语言处理基础接口服务类，提供句法分析、实体链接、事件抽取等功能。
    """
    def __init__(self):
        self.client = get_nlp_client()  # 初始化NLP客户端


    def dependency_parser(self, text, lang="zh"):
        """
        句法分析接口。
        
        :param text: 待分析的文本
        :param lang: 语言
        :return: 句法分析结果
        """
        try:
            request = RunDependencyParserRequest()
            request.body = DependencyParserRequest(
                lang=lang,
                text=text
            )
            response = self.client.run_dependency_parser(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def entity_linking(self, text, lang="zh"):
        """
        实体链接接口。
        
        :param text: 待分析的文本
        :param lang: 语言
        :return: 实体链接结果
        """
        try:
            request = RunEntityLinkingRequest()
            request.body = PostEntityLinkingRequest(
                lang=lang,
                text=text
            )
            response = self.client.run_entity_linking(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def event_extraction(self, text):
        """
        事件抽取接口。
        
        :param text: 待分析的文本
        :return: 事件抽取结果
        """
        try:
            request = RunEventExtractionRequest()
            request.body = PostEventExtractionReq(
                text=text
            )
            response = self.client.run_event_extraction(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def keyword_extract(self, text, lang="zh", limit=5):
        """
        关键词抽取接口。
        
        :param text: 待分析的文本
        :param lang: 语言
        :param limit: 抽取关键词数量限制
        :return: 关键词抽取结果
        """
        try:
            request = RunKeywordExtractRequest()
            request.body = KeywordExtractReq(
                lang=lang,
                limit=limit,
                text=text
            )
            response = self.client.run_keyword_extract(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def multigrained_segment(self, text, lang="zh", granularity=None):
        """
        多粒度分词接口。
        
        :param text: 待分词的文本
        :param lang: 语言
        :param granularity: 分词粒度
        :return: 多粒度分词结果
        """
        try:
            request = RunMultiGrainedSegmentRequest()
            request.body = PostMultiGrainedSegmentReq(
                granularity=granularity,
                lang=lang,
                text=text
            )
            response = self.client.run_multi_grained_segment(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def ner(self, text, lang="zh"):
        """
        命名实体识别接口。
        
        :param text: 待识别的文本
        :param lang: 语言
        :return: 命名实体识别结果
        """
        try:
            request = RunNerRequest()
            request.body = NerRequest(
                lang=lang,
                text=text
            )
            response = self.client.run_ner(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def ner_domain(self, text, lang="zh", domain="general"):
        """
        领域特定命名实体识别接口。
        
        :param text: 待识别的文本
        :param lang: 语言
        :param domain: 领域类型
        :return: 领域特定命名实体识别结果
        """
        try:
            request = RunNerDomainRequest()
            request.body = PostDomainNerRequest(
                domain=domain,
                lang=lang,
                text=text
            )
            response = self.client.run_ner_domain(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def segment(self, text, lang="zh", pos_switch=0, criterion="PKU"):
        """
        分词接口。
        
        :param text: 待分词的文本
        :param lang: 语言
        :param pos_switch: 是否启用词性标注
        :param criterion: 分词标准
        :return: 分词结果
        """
        try:
            request = RunSegmentRequest()
            request.body = SegmentRequest(
                criterion=criterion,
                lang=lang,
                pos_switch=pos_switch,
                text=text
            )
            response = self.client.run_segment(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def sentence_embedding(self, sentences, domain="general"):
        """
        句向量生成接口。
        
        :param sentences: 待生成句向量的文本列表
        :param domain: 领域类型
        :return: 句向量生成结果
        """
        try:
            request = RunSentenceEmbeddingRequest()
            request.body = PostSentenceEmbeddingReq(
                domain=domain,
                sentences=sentences
            )
            response = self.client.run_sentence_embedding(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def text_similarity(self, text1, text2, lang="zh"):
        """
        文本相似度接口。
        
        :param text1: 待比较的文本1
        :param text2: 待比较的文本2
        :param lang: 语言
        :return: 文本相似度结果
        """
        try:
            request = RunTextSimilarityRequest()
            request.body = TextSimilarityRequest(
                lang=lang,
                text2=text2,
                text1=text1
            )
            response = self.client.run_text_similarity(request)
            return response.to_dict()
        except exceptions.ClientRequestException as e:
            print_error(e)
            return None

    def text_similarity_advance(self, text1, text2, lang="zh"):
        """
        高级文本相似度接口。
        
        :param text1: 待比较的文本1
        :param text2: 待比较的文本2
        :param lang: 语言
        :return: 高级文本相似度结果
        """
        try:
            request = RunTextSimilarityAdvanceRequest()
            request.body = TextSimilarityAdvanceRequest(
                lang=lang,
                text2=text2,
                text1=text1
            )
            response = self.client.run_text_similarity_advance(request)
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