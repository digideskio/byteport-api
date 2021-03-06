#!/usr/bin/env python
__author__ = 'hans'

from setuptools import setup

setup(name='Byteport API',
      version='0.61',
      description='Python Clients for Byteport (www.byteport.se)',
      author='Byteport developers',
      author_email='contact@byteport.se',
      url='https://github.com/iGW/byteport-api',
      packages=['byteport'],
      install_requires=[
            'pytz>=2015.7',
            'stompest==2.1.6',
            'paho-mqtt==1.1'
      ]
)
