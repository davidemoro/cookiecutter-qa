#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(*filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, *filepath))


def remove_folder(*folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, *folderpath))


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs', 'authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        remove_file('{{ cookiecutter.project_slug }}', 'cli.py')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.testrail }}' == 'n':
        remove_file('testrail.cfg')

    if '{{ cookiecutter.advanced }}' == 'n':
        remove_folder('{{cookiecutter.project_slug}}', 'pages')
        remove_folder('{{cookiecutter.project_slug}}', 'features')
        remove_file('{{cookiecutter.project_slug}}', 'config.py')
        remove_file('{{cookiecutter.project_slug}}', 'cli.py')
        remove_file('{{cookiecutter.project_slug}}', 'tests',
                    'functional', 'test_login.py')
        remove_file('{{cookiecutter.project_slug}}', 'tests',
                    'functional', 'test_logout.py')
        remove_file('{{cookiecutter.project_slug}}', 'tests',
                    'functional', 'conftest.py')
