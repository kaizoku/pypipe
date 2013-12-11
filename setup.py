#!/usr/bin/env python

from setuptools import setup

setup(name		    = 'pypipe',
      version		= '0.1',
      description	= 'Tests the given webserver for enabled HTTP methods.',
      author		= 'kaizoku',
      author_email	= 'kaizoku@phear.cc',
      py_modules	= ['pypipe'],
      license		= 'WTF',
      url		    = 'http://github.com/kaizoku/pypipe',
      entry_points  = {
          'console_scripts': ['pypipe = pypipe:main']
          },
)
