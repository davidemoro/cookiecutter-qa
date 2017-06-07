from setuptools import setup, find_packages

version = '{{ cookiecutter.version }}dev'


install_requires = [
    'pytest-bdd',
    'pytest-splinter',
    'pytest-variables[yaml]',
    'pypom_form',
    # 'pytest-pypom-navigation',
    'colander',
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
