# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_todo.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-todo',
    version=get_version(),
    description="TODO notes checker, plugin for flake8",  # noqa
    long_description=get_long_description(),
    keywords='flake8 todo',
    author='Marc Schlaich',
    author_email='marc.schlaich@gmail.com',
    url='https://github.com/schlamar/flake8-todo',
    license='MIT',
    py_modules=['flake8_todo'],
    install_requires=[
        'pycodestyle >= 2.0.0, < 3.0.0'
    ],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'T000 = flake8_todo:check_todo_notes',
        ],
    },
    classifiers=[
        'Framework :: Flake8',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
