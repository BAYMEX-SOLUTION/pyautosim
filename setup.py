from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyautosim',
    version='0.1',
    description='automation simulation library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BAYMEX-SOLUTION/pyautosim',
    author='BAYMEX SOLUTION',
    keywords='automation simulation',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.4, <4',
)
