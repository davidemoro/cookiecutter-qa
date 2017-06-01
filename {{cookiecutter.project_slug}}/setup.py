from setuptools import setup, find_packages

version = '0.0.1dev'


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
      description="Tierra QA",
      long_description=open("README.rst").read() + "\n" +
      open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pytest",
          "Topic :: Software Development :: Testing",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: PyPy",
          ],
      keywords='',
      author='Tierra QA Team',
      author_email='DLQA@tierratelematics.com',
      url='http://tierratelematics.com',
      license='Apache License, Version 2.0',
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
