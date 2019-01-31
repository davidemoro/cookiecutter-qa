from setuptools import setup, find_packages

version = '{{ cookiecutter.version }}dev'


install_requires = [
    'pytest-pypom-navigation',
    'colander',
    'pytest-variables[yaml]',
    'pytest-bdd',
    'pytest-splinter',
    'pypom_form',
{%- if cookiecutter.testrail == 'y' %}
    'pytest-testrail',
{%- endif %}
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    'Click>=6.0',
    {%- endif %}
]

{%- if cookiecutter.pytest_play == 'y' %}
play_require = [
    'pytest-play',
    'play_selenium',
    'play_requests',
    # 'play_sql',
    # 'play_cassandra',
    # 'play_dynamodb',
    # 'play_websocket',
    # 'play_mqtt',
]
{%- endif %}

tests_require = [
    'pycodestyle',
    'pytest-cov',
    'tox',
    'mock',
    'pytest-html',
    'pytest-repeat',
    'pytest-randomly',
]

docs_require = [
    'Sphinx',
    'sphinx_rtd_theme',
    ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(name='{{cookiecutter.project_slug}}',
      version=version,
      description="{{ cookiecutter.project_short_description }}",
      long_description=open("README.rst").read() + "\n" +
      open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Intended Audience :: Developers",
          "Framework :: Pytest",
          "Topic :: Software Development :: Testing",
{%- if cookiecutter.open_source_license in license_classifiers %}
          '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: PyPy",
          ],
      keywords='{{ cookiecutter.project_slug }}',
      author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
{%- if cookiecutter.open_source_license in license_classifiers %}
      license="{{ cookiecutter.open_source_license }}",
{%- endif %}
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      {%- if 'no' not in cookiecutter.command_line_interface|lower %}
      entry_points={
          'console_scripts': [
              '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main'
          ]
      },
      {%- else %}
      entry_points="""
      # -*- Entry points: -*-
      """,
      {%- endif %}
      extras_require={
          'docs': docs_require,
          'tests': tests_require,
{%- if cookiecutter.pytest_play == 'y' %}
          'play': play_require,
{%- endif %}
          },
      )
