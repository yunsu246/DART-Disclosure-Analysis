# OpenLawData-Crawling

## 개요
* [기업공시시스템 OPEN API](http://dart.fss.or.kr "DART 홈페이지로 이동")로부터 각종 공시정보(재무제표, 사업의 내용 등등)의 Raw Data를 조회/저장하기 위한 코드 입니다.

## API 구조
* 조건: API KEY 발급 후 사용가능

## 구분 및 기능
* [KrxCorpList](https://github.com/yunsu246/DART-Disclosure-Analysis/tree/master/crawler/KrxCorpList "KrxCorpList"): `한국거래소(KRX) > 상장기업 정보(리스트)`를 조회/저장
* [DartDisclosureRptCnt](https://github.com/yunsu246/DART-Disclosure-Analysis/tree/master/crawler/DartDisclosureRptCnt "DartDisclosureRptCnt"): `KrxCorpList`로부터 `한국거래소(KRX) > 상장기업 정보(리스트)`이 저장될 때를 `event`로 받아와 `기업공시시스템 OPEN API > 공시데이터`를 조회하여 저장

## 주요 리소스 및 아키텍쳐
* Serverless: AWS(S3, ECS(Fargate), Lambda)
* Crawler: Python(asyncio, aiohttp, arsenic)
* TEST environment: docker(alpine), lambdaCI([docker-lambda](https://github.com/lambci/docker-lambda "docker-lambda"))
* CI/CD: aws-cli, zappa

* Diagram
    - 준비중