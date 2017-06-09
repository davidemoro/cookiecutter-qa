FROM python:3.6-alpine

COPY . /src
WORKDIR /src

RUN pip3 install --upgrade pip \
        setuptools \
        tox

# TODO: remove me when pypom_navigation will be released
RUN apk add --no-cache git && \
    rm -fR /root/.cache

ENTRYPOINT [ "tox"]
CMD ["-epy36",  "--", "-vvv", "--splinter-webdriver=remote", "--variables=credentials_template.yml", "--splinter-remote-url=http://{{cookiecutter.browserstack_username}}:{{cookiecutter.browserstack_access_key}}@hub.browserstack.com:80/wd/hub", "--variables=capabilities/WIN10-IE.json"]
