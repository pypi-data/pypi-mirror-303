from setuptools import setup, find_packages

with open('README') as f:
    long_description = f.read()

setup(
    name='util_rc',
    author='Donna Ma',
    author_email='donna.ma@berkeley.edu',
    description='A PyPI package to model risky choice',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.1',
    packages=find_packages(),
)