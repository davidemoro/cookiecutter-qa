import pytest
from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree


BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME', "davidemoro2")
BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY', '')

selenium_grid_url = 'http://{0}:{1}@hub.browserstack.com:80/wd/hub'.format(
    BROWSERSTACK_USERNAME,
    BROWSERSTACK_ACCESS_KEY,
)


@pytest.fixture
def default_extra_context():
    return {
        'selenium_grid_url': selenium_grid_url,
    }


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its
                    temporalfiles will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        if os.getenv('TRAVIS'):
            with open(os.devnull, 'w') as devnull:
                return subprocess.check_call(shlex.split(command),
                                             stdout=devnull,
                                             stderr=devnull)
        else:
            return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'pytest.ini' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'credentials' in found_toplevel_files
        assert 'testrail.cfg' in found_toplevel_files

        credential_files = [
            subitem.basename for subitem in
            [item for item in result.project.visit(
                'credentials')][0].listdir()]
        assert 'credentials_template.yml' in credential_files

        found_secondlevel_files = [
            subitem.basename for subitem in
            [item for item in result.project.visit('project_qa')][0].listdir()]
        assert 'tests' in found_secondlevel_files
        assert '__init__.py' in found_secondlevel_files
        assert 'config.py' in found_secondlevel_files
        assert 'pages' in found_secondlevel_files
        assert 'features' in found_secondlevel_files

        setup_py_path = [f.strpath for f in result.project.listdir()
                         if f.basename == 'setup.py'][0]
        with open(setup_py_path) as setup_py_file:
            assert 'pytest-testrail' in setup_py_file.read()


def test_bake_with_testrail(cookies):
    """ testrail support """
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        setup_py_path = [f.strpath for f in result.project.listdir()
                         if f.basename == 'setup.py'][0]
        with open(setup_py_path) as setup_py_file:
            assert 'pytest-testrail' in setup_py_file.read()


def test_bake_without_testrail(cookies):
    """ testrail support """
    with bake_in_temp_dir(cookies, extra_context={'testrail': "n"}) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'testrail.cfg' not in found_toplevel_files

        setup_py_path = [f.strpath for f in result.project.listdir()
                         if f.basename == 'setup.py'][0]
        with open(setup_py_path) as setup_py_file:
            assert 'pytest-testrail' not in setup_py_file.read()


def test_bake_and_run_tests(cookies, default_extra_context):
    extra_context = default_extra_context.copy()
    with bake_in_temp_dir(
            cookies,
            extra_context=extra_context) as result:
        assert result.project.isdir()
        project_path = str(result.project)
        run_inside_dir(
            'docker run --rm -i -v {0}:/src davidemoro/pytest-play '
            '--splinter-remote-url={1}'.format(
                project_path,
                default_extra_context['selenium_grid_url']),
            str(result.project)) == 0
        print("test_bake_and_run_tests path", project_path)


def test_bake_with_no_testrail_and_run_tests(cookies, default_extra_context):
    """Ensure that an without testrail doesn't break things"""
    extra_context = default_extra_context.copy()
    extra_context['testrail'] = "n"
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project.isdir()
        project_path = str(result.project)
        run_inside_dir(
            'docker run --rm -i -v {0}:/src davidemoro/pytest-play '
            '--splinter-remote-url={1}'.format(
                project_path,
                default_extra_context['selenium_grid_url']),
            str(result.project)) == 0


def test_bake_with_no_play_and_run_tests(cookies, default_extra_context):
    """Ensure that an without testrail doesn't break things"""
    extra_context = default_extra_context.copy()
    extra_context['pytest_play'] = "n"
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project.isdir()
        project_path = str(result.project)
        run_inside_dir(
            'docker run --rm -i -v {0}:/src davidemoro/pytest-play '
            '--splinter-remote-url={1}'.format(
                project_path,
                default_extra_context['selenium_grid_url']),
            str(result.project)) == 0
