#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-mechanize',
    version='0.1',
    description='Mechanize support for Django test cases',
    long_description=open('README.rst').read(),
    author='Nathan Reynolds',
    url='http://nreynolds.co.uk/django-mechanize/',
    packages=['djangomechanize'],
    install_requires=[line.strip() for line in open('requirements.txt')],
    test_suite='tests',
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ],
)
