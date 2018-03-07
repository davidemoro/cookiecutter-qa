#!/usr/bin/env python

import re
import os
import sys
import subprocess
try:
    from shlex import quote
except ImportError:
    from pipes import quote


def quoted_args(args):
    for arg in args:
        if re.match('^[.:/\-\w]+$', arg):
            yield arg
        else:
            yield quote(arg)


if __name__ == "__main__":
    environment = os.getenv('ENVIRONMENT')
    markers = os.getenv('MARKERS')
    keywords = os.getenv('KEYWORDS')
    os_version = os.getenv('OS')
    browser = os.getenv('BROWSER')
    parallel_sessions = os.getenv('PARALLEL_SESSIONS')
    count = os.getenv('COUNT')
    junit_output = 'results/{0}.xml'.format(os.getenv('BUILD_ID'))
    grid_url = os.getenv('SELENIUM_GRID_URL', '')
    fallback_grid_url = '{{cookiecutter.selenium_grid_url}}'
    selenium_grid_url = grid_url or fallback_grid_url
    play = os.getenv('PLAY')

    os_file = 'capabilities/{0}'.format(os_version)
    browser_file = 'capabilities/{0}'.format(browser)
    resolution_file = 'capabilities/{0}'.format(os.getenv('RESOLUTION'))
    credentials_file = 'credentials/credentials-{0}.yml'.format(environment)

    pytest_cmd = [
        "tox",
        "-epy36",
        "--",
        "-vvv",
        "--variables",
        "capabilities/project.json",
        "--variables",
        os_file,
        "--variables",
        browser_file,
        "--variables",
        resolution_file,
        "--splinter-webdriver",
        "remote",
        "--splinter-remote-url",
        selenium_grid_url,
        "--variables",
        credentials_file,
        "--junitxml",
        junit_output,
    ]

    if play:
        with open(
                os.path.join('{{cookiecutter.project_slug}}',
                             'tests',
                             'data',
                             'play.json'),
                'w') as file_obj:
            file_obj.write(play)

    if markers:
        pytest_cmd.extend([
            "-m",
            markers,
        ])

    if keywords:
        pytest_cmd.extend([
            "-k",
            keywords
        ])

    if os.getenv('DEBUG') == 'true':
        pytest_cmd.extend([
            "--variables",
            "capabilities/debug.json"
        ])

    if os.getenv('TESTRAIL_ENABLE') == 'true':
        testrail_file = 'testrail.cfg'
        assert os.path.isfile(testrail_file)

        tr_name = '[{0}][{1}][{2}][{3}][{4}]'.format(
            environment, os_version, browser, markers, keywords)

        pytest_cmd.extend([
            "--testrail",
            "--tr-config",
            testrail_file,
            "--tr-testrun-name",
            tr_name,
        ])

    if os.getenv('BLOCK_FIRST_FAILURE') == 'true':
        pytest_cmd.append('-x')

    if parallel_sessions:
        pytest_cmd.extend([
            "-n",
            parallel_sessions,
        ])

    if count and count > 0:
        pytest_cmd.extend([
            "--count",
            count,
        ])

    pytest_cmd.extend(sys.argv[1:])

    print(" ".join(quoted_args(pytest_cmd)))
    subprocess.check_call(pytest_cmd)
