#-- coding:utf-8 --
import os


class Config(object):

    # ---------------------[ Custom Parameters Variables in src.main.py ]-----------------------
    # Custom Parameters
    HOST = 'http://dart.fss.or.kr'
    HOST_MAIN = '/'.join([HOST, 'dsaf001', 'main.do'])
    HOST_REPORT_VIEWER = '/'.join([HOST, 'report', 'viewer.do'])
    RPT_CNT = ['II. 사업의 내용']    
    # ------------------------------------------------------------------------------------------

    # ---------------------[ Custom Parameters in src.modules.crawler.py ]----------------------
    CHROME_PATH = '/usr/lib/chromium'
    BINARY_PATH = {
        # "CHROME_BROWSER": os.path.join(CHROME_PATH, 'chrome')
        "CHROME_DRIVER": os.path.join(CHROME_PATH, 'chromedriver'),
    }
    # ------------------------------------------------------------------------------------------
    