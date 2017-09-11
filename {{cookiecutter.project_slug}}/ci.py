#!/usr/bin/env python

import os
from shlex import split

try:
    from shlex import quote
except ImportError:
    from pipes import quote

from subprocess import check_call


def prettify_path(path):
    return path.split('/')[-1].replace('.json', '')


if __name__ == "__main__":
    environment = os.getenv('ENVIRONMENT')
    markers = os.getenv('MARKERS')
    keywords = os.getenv('KEYWORDS')
    os_version = os.getenv('OS')
    browser = os.getenv('BROWSER')
    parallel_sessions = os.getenv('PARALLEL_SESSIONS')
    build_id = quote('results/{0}.xml'.format(os.getenv('BUILD_ID')))
    grid_url = os.getenv('SELENIUM_GRID_URL', '')
    fallback_grid_url = 'http://{0}:{1}@hub.browserstack.com:80/wd/hub'.format(
        '{{cookiecutter.browserstack_username}}',
        '{{cookiecutter.browserstack_access_key}}',
    )
    selenium_grid_url = grid_url and quote(grid_url) or fallback_grid_url

    os_file = 'capabilities/{0}'.format(os_version)
    browser_file = 'capabilities/{0}'.format(browser)
    resolution_file = 'capabilities/{0}'.format(
        os.getenv('RESOLUTION'))
    credentials_file = 'credentials/credentials-{0}.yml'.format(environment)

    assert os.path.isfile(os_file)
    assert os.path.isfile(browser_file)
    assert os.path.isfile(resolution_file)
    assert os.path.isfile(credentials_file)

    pytest_cmd = [
        "tox",
        "-epy36",
        "--",
        "-vvv",
        "--variables",
        "capabilities/project.json",
        "--variables",
        "{0}".format(os_file),
        "--variables",
        "{0}".format(browser_file),
        "--variables",
        "{0}".format(resolution_file),
        "--splinter-webdriver",
        "remote",
        "--splinter-remote-url",
        "{0}".format(
            selenium_grid_url),
        "--variables",
        "{0}".format(credentials_file),
        "--junitxml",
        "{0}".format(build_id),
    ]

    if markers:
        pytest_cmd.extend([
            "-m",
            quote(markers),
        ])

    if keywords:
        pytest_cmd.extend([
            "-k",
            quote(keywords)
        ])

    if os.getenv('DEBUG') == 'true':
        pytest_cmd.extend([
            "--variables",
            "capabilities/debug.json"
        ])

    if os.getenv('TESTRAIL_ENABLE') == 'true':
        if 'pcmw' in environment:
            env = 'pcmw'
        else:
            env = 'sust'

        testrail_file = 'conf/testrail/testrail-{0}.cfg'.format(env)
        assert os.path.isfile(testrail_file)

        tr_name = quote('[{0}][{1}][{2}][{3}][{4}]'.format(
            prettify_path(environment), prettify_path(os_version),
            prettify_path(browser), markers, keywords))

        pytest_cmd.extend([
            "--testrail",
            testrail_file,
            "--tr_name",
            tr_name,
        ])

    if os.getenv('BLOCK_FIRST_FAILURE') == 'true':
        pytest_cmd.append('-x')

    if parallel_sessions:
        assert isinstance(parallel_sessions, int)
        pytest_cmd.extend([
            "-n",
            parallel_sessions,
        ])

    check_call(split(" ".join(pytest_cmd)))
