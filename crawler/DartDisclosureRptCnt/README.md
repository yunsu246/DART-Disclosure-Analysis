## Tree
```bash
DartDisclosureRptCnt
    ├── lib: 설치된 Python 라이브러리 저장소
    ├── src
    │     ├── main.py: 크롤러 실행 스크립트
    │     ├── config.py: configure 모음
    │     └── modules: 크롤러 실행을 위한 모듈 모음
    │              ├── crawler.py: DART 공시정보 API 호출 결과 조회/저장 등 크롤링 프로세스 관리
    │              └── webdriver
    │                        └── chromedriver.py: arsenic(async + selenium)과 chromedriver 간 연결(session) 관리
    │
    ├── Dockerfile: Docker image(구성) 정의
    ├── requirements.txt: Python 라이브러리 관리
    └── Makefile: Local Development & Deployment 명령어 관리
```

## Configures (./src/config.py 참조)

## Bash shell (./Makefile)

* 참고사항
    - `AWS_ACCOUNT_ID`: AWS 사용자 계정 ID (숫자) 

## Local Development Env Setup & Deployment

``` bash
# clear up caches
make clean

# build docker image
make docker-build

# run docker container
make docker-run

# push docker image to AWS ECR registry
make docker-push
```