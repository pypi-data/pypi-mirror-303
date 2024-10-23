from .utils.bbc import bbc_news as get_bbc_news
from .utils.abp_news import abp_news as get_abp_news
from .utils.india_today import india_today as get_india_today


class NewsAPI:
    def __init__(self):
        pass

    def bbc(self, query=None):
        return get_bbc_news(query)

    def abp(self, query=None):
        return get_abp_news(query)

    def india_today(self, query=None):
        return get_india_today(query)
