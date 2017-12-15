FROM python:3.6-alpine

COPY . /src
WORKDIR /src


RUN pip3 install --upgrade pip \
        tox && \
    apk update && \
    apk add git

ENTRYPOINT [ "tox"]
CMD ["-epy36",  "--", "-vvv", "--splinter-webdriver=remote", "--variables=credentials_template.yml", "--splinter-remote-url={{cookiecutter.selenium_grid_url}}", "--variables=capabilities/os/WIN10.json", "--variables=capabilities/browsers/chrome/CHROME59.json", "--variables=capabilities/resolutions/1280x1024.json"]
