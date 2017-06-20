# !/usr/bin/env python

from distutils.core import setup


tests_require = [
    'click',
    'cookiecutter>=1.4.0',
    'pytest',
    'pytest-cookies',
    'tox',
]

docs_require = [
    'Sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='cookiecutter-qa',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a QA package',
    author='Davide Moro',
    license='BSD',
    author_email='davide.moro@gmail.com',
    url='https://github.com/tierratelematics/cookiecutter-qa',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
        },
)
