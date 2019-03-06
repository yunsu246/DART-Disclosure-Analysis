#-- coding:utf-8 --
import os
import re
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from modules.webdriver.chromedriver import AsyncWebDriverWrapper


class AsyncDartDisclosureCrawler():

    def __init__(self, hostMain, hostReportViewer, max_concurrency=5):
        self.hostMain= hostMain
        self.hostReportViewer = hostReportViewer
        self.boundedSempahore = asyncio.BoundedSemaphore(max_concurrency)
    
    @AsyncWebDriverWrapper()
    async def fetchHtmlResponse(self, session, uri):
        try:
            await session.get(uri)
            await asyncio.sleep(3)
            html = await session.get_page_source()
            return html
        except Exception as err:
            raise err

    def parseHtmlTreeNode(self, html):
        treeNode = re.findall(r'TreeNode\(\{.*?\}\)\;', html, re.I|re.S)[1:] #목차 내용만 추출
        return treeNode

    def convertHtmlTreeNodeItemToJson(self, node):
        item = dict()
        item['rpt_cnt'] = re.search(r'text\:.*?\,', node).group()[7:-2]
        item['id'] = re.search(r'id\:.*?\,', node).group()[5:-2]
        item['cls'] = re.search(r'cls\:.*?\,', node).group()[6:-2]
        listenersKey = ['rcpNo', 'dcmNo', 'eleId', 'offset', 'length', 'dtd']
        listenersValue = re.search(r'\{viewDoc\(.*?\}', node, re.I|re.S).group()[9:-3]
        listenersValue = re.sub(r'[\s\']', '', listenersValue).split(',')
        listeners = {key:value for key, value in zip(listenersKey, listenersValue)}
        item = {**item, **listeners}
        hyperlink = '{hostReportViewer}?rcpNo={rcpNo}&dcmNo={dcmNo}&eleId={eleId}&offset={offset}&length={length}&dtd={dtd}'.format(
            hostReportViewer=self.hostReportViewer, **listeners
        )
        item['hyperlink'] = hyperlink
        return item

    async def convertHtmlTreeNodeToDataFrame(self, rcpNo, rptCnt):
        with (await self.boundedSempahore):
            uri = f'{self.hostMain}?rcpNo={rcpNo}'
            req = await self.fetchHtmlResponse(uri=uri)
            treeNode = self.parseHtmlTreeNode(req)

            treeNodeList = []
            for node in treeNode:
                item = self.convertHtmlTreeNodeItemToJson(node)
                item['crp_cd'] = rcpNo
                treeNodeList.append(item)
            
            df = pd.DataFrame(treeNodeList)
            df = df.loc[df['rpt_cnt'].isin([*rptCnt])]

        return df    

    async def concatDartDisclosureInfoList(self, corpInfo, rptCnt):
        rcpNoList = corpInfo['crp_cd']
        DartDisclosureInfoList = [self.convertHtmlTreeNodeToDataFrame(rcpNo, rptCnt) for rcpNo in rcpNoList]
        DartDisclosureInfoIter = asyncio.as_completed(DartDisclosureInfoList)

        df = pd.DataFrame()
        for future in DartDisclosureInfoIter:
            df = pd.concat([df, await future])

        return df
        