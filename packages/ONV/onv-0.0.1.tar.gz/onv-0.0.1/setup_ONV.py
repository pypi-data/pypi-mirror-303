from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Package for general NV based simulations'
LONG_DESCRIPTION = 'A basic package of functions which are commonly used in the simuitons of NV centers fro quantum computing and NMR sensing'

setup(
      name = 'ONV',
      version = VERSION,
      author = 'Oliver Whaites',
      author_email = 'o.whaites@btinternet.com',
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      packages = find_packages(),
      install_requires = [],
      
      keywords = ['NV'],
      classifiers = ['Development Status :: 3 - Alpha',
                     'Intended Audience :: Education',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 3',
                     'Operating System :: MacOS :: MacOS X',
                     'Operating System :: Microsoft :: Windows']
      )