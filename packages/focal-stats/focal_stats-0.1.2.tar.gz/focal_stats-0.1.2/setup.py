import os

from setuptools import setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name='focal_stats',
    version='0.1.2',
    url='',
    license='MIT',
    author='Jasper Roebroek',
    author_email='roebroek.jasper@gmail.com',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
)
