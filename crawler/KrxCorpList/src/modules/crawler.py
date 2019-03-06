#-- coding:utf-8 --
import asyncio
import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import pandas as pd


class AsyncKrxCorpListCrawler():
    def __init__(self, host, method, searchType, industry, fiscalYearEnd, location, marketType, max_concurrency=10):
        self.host = host
        self.method = method
        self.searchType = searchType
        self.industry = industry
        self.fiscalYearEnd = fiscalYearEnd
        self.location = location
        self.marketType = marketType
        self.marketTypeList = (marketType[key] for key in self.marketType.keys() if key != "rAll")
        self.boundedSempahore = asyncio.BoundedSemaphore(max_concurrency)

    async def fetchHtmlResponse(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        html = await response.content.read()
                        return html
                    else:
                        return {'error': response.status, 'html': ''}
            except Exception as err:
                return {'error': err, 'html': ''}
                    
    def parseHtmlTable(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find_all('table')[0]
        return table

    async def convertHtmlTableToDataFrame(self, marketType):
        try:
            with (await self.boundedSempahore):
                uri = f'{self.host}?method={self.method}&searchType={self.searchType}&industry={self.industry}&fiscalYearEnd={self.fiscalYearEnd}&location={self.location}&marketType={marketType}'
                req = await self.fetchHtmlResponse(uri)
                table = self.parseHtmlTable(req)
                df = pd.read_html(str(table), header=0)[0]
                df['marketType'] = marketType
                df['종목코드'] = df['종목코드'].astype(str).str.zfill(6)
            return df
        
        except Exception as err:
            return {'error': err, 'table': pd.DataFrame()}

    async def concatKRXCorpList(self):
        KRXCorpDataFrameList = [self.convertHtmlTableToDataFrame(marketType) for marketType in self.marketTypeList]
        KRXCorpDataFrameIter = asyncio.as_completed(KRXCorpDataFrameList)

        df = pd.DataFrame()
        for future in KRXCorpDataFrameIter:
            df = pd.concat([df, await future])

        return df