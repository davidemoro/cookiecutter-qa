from setuptools import setup, find_packages

version = '{{ cookiecutter.version }}dev'


install_requires = [
{%- if cookiecutter.advanced  == 'y' %}
    'pytest-pypom-navigation',
    'colander',
    'pytest-variables[yaml]',
    'pytest-bdd',
    'pytest-splinter',
    'pypom_form',
{% else %}
    'pytest-selenium',
{%- endif %}
{%- if cookiecutter.testrail == 'y' %}
    'pytest-testrail',
{%- endif %}
]

tests_require = [
    'pycodestyle',
    'pytest-cov',
    'tox',
    'mock',
    'pytest-html',
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
      entry_points="""
      # -*- Entry points: -*-
      """,
      extras_require={
          'docs': docs_require,
          'tests': tests_require,
          },
      )
