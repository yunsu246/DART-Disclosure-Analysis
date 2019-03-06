FROM python:3.7-alpine3.8

USER root

RUN mkdir -p /DART-Disclosure-Analysis
ENV APP_DIR /DART-Disclosure-Analysis
WORKDIR $APP_DIR

# update apk repo ('echo': stable, 'echo @edge': latest)
RUN echo @edge "http://dl-4.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo @edge "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

# install chromium & chromedriver (@edge: latest)
RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver

# install required SOFTWARE PACKAGES for numpy installation
RUN apk add --no-cache --virtual build-dependencies alpine-sdk

ENV PYTHON_DEV_PACKAGES="\
    arsenic \
    beautifulsoup4 \
    numpy \
"
ENV PYTHON_PACKAGES="\
    pandas \
"

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir $PYTHON_DEV_PACKAGES
RUN pip install --no-cache-dir $PYTHON_PACKAGES

COPY src ./src
VOLUME ./src/:$APP_DIR/src/

CMD ["python3", "src/main.py"]


  

