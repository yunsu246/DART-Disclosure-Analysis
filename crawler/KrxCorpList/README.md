## Tree
```bash
KrxCorpList
    ├── lib: 설치된 Python 라이브러리 저장소(for Local Development)
    ├── src
    │     ├── lambda_function.py: 크롤러 실행 스크립트
    │     ├── config.py: configure 모음
    │     └── modules: 크롤러 실행을 위한 모듈 모음
    │              └── crawler.py: OPEN API 호출/결과 조회/저장 등 크롤링 프로세스 관리
    │
    ├── docker-compose: Docker container의 실행환경 정의(for Local Development)
    ├── Dockerfile: Docker image(구성) 정의(for Local Development)
    ├── requirements.txt: Python 라이브러리 관리(for Local Development)
    ├── Pipfile: pipenv를 사용한 Python virtualenv & 라이브러리 의존성 관리(for Deployment)
    ├── zappa_settings.json: zappa deploy & zappa update 시 필요한 settings(for Deployment) 
    └── Makefile: Local Development 시 명령어 관리
```

## Configures (./src/config.py)

* Custom Parameters
    * CRAWLER_CONFIG: KRX Back-End API 호출 시 필요정보 

## Deployment Settings (./zappa_settings.json)

* OPTIONAL, otherwise start with `zappa init`

* dev
    - s3_bucket: Pre-created s3 bucket for deploying application from s3 bucket to AWS Lambda.

## Local Development Env Setup

``` bash
# clear up caches
make clean

# build docker image
make docker-build

# run docker container
make docker-run
```

## Deployment

``` bash
# install dependencies
pipenv install

# start virtual environment mode
pipenv shell

# deploy application
zappa deploy

# update deployed application
zappa update
```