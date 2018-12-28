#!/usr/bin/env python
from setuptools import find_packages, setup
import versioneer

README = open('README.rst', 'r').read()


setup(
    name='python-language-server',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Python Language Server for the Language Server Protocol',

    long_description=README,

    # The project's main homepage.
    url='https://github.com/palantir/python-language-server',

    author='Palantir Technologies, Inc.',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'test']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'configparser; python_version<"3.0"',
        'future',
        'futures; python_version<"3.2"',
        'jedi',
        'python-jsonrpc-server',
        'pluggy',
        'autopep8',
        'mccabe',
        'pycodestyle',
        'pydocstyle',
        'pyflakes',
        'rope',
        'yapf',
        'pyls-isort',
        'pyls-black',
        'black',
    ],

    dependency_links=[
        'hg+https://bitbucket.org/ambv/configparser@default#egg=configparser'
        'git+https://github.com/PythonCharmers/python-future@master#egg=future',
        'git+https://github.com/agronholm/pythonfutures@master#egg=futures',
        'git+https://github.com/zchee/jedi@typeshed-dev#egg=jedi',
        'git+https://github.com/palantir/python-jsonrpc-server@master#egg=python-jsonrpc-server',
        'git+https://github.com/pytest-dev/pluggy@master#egg=pluggy',
        'git+https://github.com/hhatto/autopep8@master#egg=autopep8',
        'git+https://github.com/PyCQA/mccabet@master#egg=mccabe',
        'git+https://github.com/PyCQA/pycodestyle@master#egg=pycodestyle',
        'git+https://github.com/PyCQA/pydocstyle@master#egg=pydocstyle',
        'git+https://github.com/PyCQA/pyflakes@master#egg=pyflakes',
        'git+https://github.com/python-rope/rope@master#egg=rope',
        'git+https://github.com/google/yapf@master#egg=yapf',
        'git+https://github.com/tomv564/pyls-mypy@master#egg=pyls-mypy',
        'git+https://github.com/paradoxxxzero/pyls-isort@master#egg=pyls-isort',
        'git+https://github.com/rupert/pyls-black@master#egg=pyls-black',
        'git+https://github.com/ambv/black@master#egg=black'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[test]
    extras_require={
        'all': [
            'autopep8',
            'mccabe',
            'pycodestyle',
            'pydocstyle>=2.0.0',
            'pyflakes>=1.6.0',
            'rope>=0.10.5',
            'yapf',
        ],
        'autopep8': ['autopep8'],
        'mccabe': ['mccabe'],
        'pycodestyle': ['pycodestyle'],
        'pydocstyle': ['pydocstyle>=2.0.0'],
        'pyflakes': ['pyflakes>=1.6.0'],
        'rope': ['rope>0.10.5'],
        'yapf': ['yapf'],
        'test': ['tox', 'versioneer', 'pytest', 'mock', 'pytest-cov', 'coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pyls = pyls.__main__:main',
        ],
        'pyls': [
            'autopep8 = pyls.plugins.autopep8_format',
            'jedi_completion = pyls.plugins.jedi_completion',
            'jedi_definition = pyls.plugins.definition',
            'jedi_hover = pyls.plugins.hover',
            'jedi_highlight = pyls.plugins.highlight',
            'jedi_references = pyls.plugins.references',
            'jedi_signature_help = pyls.plugins.signature',
            'jedi_symbols = pyls.plugins.symbols',
            'mccabe = pyls.plugins.mccabe_lint',
            'preload = pyls.plugins.preload_imports',
            'pycodestyle = pyls.plugins.pycodestyle_lint',
            'pydocstyle = pyls.plugins.pydocstyle_lint',
            'pyflakes = pyls.plugins.pyflakes_lint',
            'rope_completion = pyls.plugins.rope_completion',
            'rope_rename = pyls.plugins.rope_rename',
            'yapf = pyls.plugins.yapf_format',
        ]
    },
)
