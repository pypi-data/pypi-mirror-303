#!/usr/bin/env python

from setuptools import setup
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='rainer',
      version='0.0.4',  # todo: make dynamic
      description='Resting stAte tIme and frequeNcy analyzER (RAINER)',
      author='Hendrik Mattern',
      # author_email='gward@python.net',
      # url='https://www.python.org/sigs/distutils-sig/',
      # packages=['scipy', 'nibabel', 'matplotlib'],
      # other arguments omitted
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
