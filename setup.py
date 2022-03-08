import sys
from setuptools import setup
from distutils.core import Extension

setup(name='passfuncc',
      version='0.0.1.dev',
      description='Experiment with how to best pass an arbitrary number of functions to C',
      author='Jo Bovy',
      author_email='bovy@astro.utoronto.ca',
      license='MIT',
      url='http://github.com/jobovy/pass-functions-to-c',
      package_dir = {'passfuncc/': ''},
      packages=['passfuncc'],
      package_data={"": ["README.md","LICENSE"]},
      include_package_data=True,
      install_requires=['numpy'],
      ext_modules=[Extension('passfuncc_c',
                             sources=['passfuncc/passfuncc.c'],
                             libraries=['m'],
                             include_dirs=['passfuncc/'])]
)