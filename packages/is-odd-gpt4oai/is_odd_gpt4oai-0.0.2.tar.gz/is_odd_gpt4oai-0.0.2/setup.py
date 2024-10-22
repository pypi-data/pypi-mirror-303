from setuptools import setup, find_packages
from os import path
work_dir = path.abspath(path.dirname(__file__))

with open(path.join(work_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='is-odd-gpt4oai',
    version='0.0.2',
    description='Check if a number is odd or even',
    # long_description=long_description,
    # url = "",
    author='mattekudacy',
    author_email='cyrus2952@gmail.com',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["openai"],
)