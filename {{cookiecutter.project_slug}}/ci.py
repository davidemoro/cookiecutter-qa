#!/usr/bin/env python
import os
try:
    from shlex import quote
except ImportError:
    from pipes import quote
try:
    from subprocess import run
except ImportError:  # py2
    from subprocess import call as run


def prettify_path(path):
    return path.split('/')[-1].replace('.json', '')


if __name__ == "__main__":
    environment = os.getenv('ENVIRONMENT')
    markers = quote(os.getenv('MARKERS'))
    keywords = quote(os.getenv('KEYWORDS'))
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
        'tox',
        '-epy36',
        '--',
        '-vvv',
        '--variables=capabilities/project.json',
        '--variables={0}'.format(os_file),
        '--variables={0}'.format(browser_file),
        '--variables={0}'.format(resolution_file),
        '--splinter-webdriver=remote',
        '--splinter-remote-url={0}'.format(
            selenium_grid_url),
        '--variables={0}'.format(credentials_file),
        '--junitxml={0}'.format(build_id),
    ]

    if markers:
        pytest_cmd.append('-m={0}'.format(markers))

    if keywords:
        pytest_cmd.append('-k={0}'.format(keywords))

    if os.getenv('DEBUG') == 'true':
        pytest_cmd.append('--variables=capabilities/debug.json')

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
            '--testrail={0}'.format(testrail_file),
            '--tr_name={0}"'.format(tr_name),
        ])

    if os.getenv('BLOCK_FIRST_FAILURE') == 'true':
        pytest_cmd.append('-x')

    if parallel_sessions:
        assert isinstance(parallel_sessions, int)
        pytest_cmd.append('-n {0}'.format(parallel_sessions))

    print(str(pytest_cmd))
    run(pytest_cmd)
