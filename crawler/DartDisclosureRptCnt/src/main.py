#-- coding:utf-8 --
import asyncio
from config import Config
from functools import wraps
from modules.crawler import AsyncDartDisclosureCrawler
from time import time


hostMain = Config.HOST_MAIN
hostReportViewer = Config.HOST_REPORT_VIEWER
rptCnt = Config.RPT_CNT
corpInfo = { 'crp_cd': ['20170331004421', '20170331004642'] * 10 }

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        m, s = divmod(end-start, 60)
        h, m = divmod(m, 60)
        print('Elapsed time: %02d:%02d:%02d' % (h, m, s))
        return result
    return wrapper

@timing
def main():
    asyncDartDisclosureCrawler = AsyncDartDisclosureCrawler(hostMain, hostReportViewer)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(asyncDartDisclosureCrawler.concatDartDisclosureInfoList(corpInfo, rptCnt))
    DartDisclosureInfo = loop.run_until_complete(task)
    print('length of DartDisclosureInfo:', len(DartDisclosureInfo))

if __name__ == '__main__':
    main()
