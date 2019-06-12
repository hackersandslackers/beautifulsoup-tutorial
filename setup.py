"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='linkbox-api',
    version='0.0.1',
    description='Generates a JSON object containing link preview information by passing a URL parameter.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/linkbox-api',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Link Scrape SEO Embed Widget',
    packages=find_packages(),
    install_requires=['requests', 'flask', 'beautifulsoup4'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/linkbox-api/issues',
        'Source': 'https://github.com/toddbirchard/linkbox-api/',
    },
)
