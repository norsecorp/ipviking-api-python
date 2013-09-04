"""Here's our handy setup script for the ipviking API"""

from setuptools import setup

setup(
      name = 'ipviking_api_python',
      version = '0.1',
      description = 'An easy-to-use wrapper for making requests to the IPViking API',
      author = 'Marcus Hoffman',
      url = 'https://github.com/norsecorp/ipviking-api-python',
      license = 'BSD',
      packages = ['ipviking_api_python', 'ipviking_api_python.helpers', 'ipviking_api_python.tests'],
      include_package_data = True,
      package_data = {'':['README.md']},
      install_requires = ['django'],
      tests_require = [],
      classifiers = ['Development Status :: 1 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD Licence',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Internet',
                     'Topic :: Network Security',
                     'Topic :: Software Development :: Libraries :: Python Modules'])