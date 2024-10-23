from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='DarkGram',
    version='0.0.1',
    description='DarkGram',
    author='vsp210',
    author_email='psv449@yandex.ru',
    packages=find_packages(),
    package_data={
        'DarkGram': ['*.py'],
    },
    install_requires=['requests>=2.32.3'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
