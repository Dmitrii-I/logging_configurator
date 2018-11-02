""" See [1] on how to write proper `setup.py` script.

[1] https://github.com/pypa/sampleproject/blob/master/setup.py
"""


from setuptools import setup
from logging_configurator import __version__


setup(
    name='logging_configurator',
    version=__version__,
    description='One-liner logging configurator for Python.',
    long_description='Configure logging in one line and fogetaboutit.',
    url='None',
    author='Dmitrii Izgurskii',
    author_email='izgurskii@gmail.com',
    license='MIT',
    keywords='logging',
    packages=['logging_configurator']
)
