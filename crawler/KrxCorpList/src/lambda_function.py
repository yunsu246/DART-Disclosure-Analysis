#-- coding:utf-8 --
import asyncio
from functools import wraps
from src.config import Config
from time import time
from modules.crawler import AsyncKrxCorpListCrawler


host = Config.CRAWLER_CONFIG['host']
method = Config.CRAWLER_CONFIG['method']
searchType = Config.CRAWLER_CONFIG['searchType']['상장법인']
industry = Config.CRAWLER_CONFIG['industry']['전체']
fiscalYearEnd = Config.CRAWLER_CONFIG['fiscalYearEnd']['전체']
location = Config.CRAWLER_CONFIG['location']['전체']
marketType = Config.CRAWLER_CONFIG['marketType']

def lambda_handler(event, context):
    start = time()
    asyncKRXCorpListCrawler = AsyncKrxCorpListCrawler(host, method, searchType, industry, fiscalYearEnd, location, marketType)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(asyncKRXCorpListCrawler.concatKRXCorpList())
    KRXCorpList = loop.run_until_complete(task)
    end = time()

    m, s = divmod(end-start, 60)
    h, m = divmod(m, 60)

    print('length of KRXCorpList:', len(KRXCorpList))
    print('Elapsed time: %02d:%02d:%02d' % (h, m, s))
