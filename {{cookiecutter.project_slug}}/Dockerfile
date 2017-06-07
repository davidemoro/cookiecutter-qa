FROM python:3.6-alpine

COPY . /src
WORKDIR /src

RUN pip3 install --upgrade pip \
        setuptools \
        tox

ENTRYPOINT [ "tox"]
CMD ["-epy36",  "--", "-vvv", "--splinter-webdriver=remote", "--variables=credentials_template.yml", "--splinter-remote-url=http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub"]
