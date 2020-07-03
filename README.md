# BeautifulSoup Web Scraping Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-v4.9.1-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Requests](https://img.shields.io/badge/Requests-v2.23.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/beautifulsoup-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/beautifulsoup-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/beautifulsoup-tutorial.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/beautifulsoup-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/beautifulsoup-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/beautifulsoup-tutorial/network)

![Beautifulsoup Tutorial](https://github.com/hackersandslackers/beautifulsoup-tutorial/blob/master/.github/beautifulsoup@2x.jpg?raw=true)

A beginner's tutorial to scraping websites using Python's [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library. This repository is the source code for the tutorial found here: 
https://hackersandslackers.com/scraping-urls-with-beautifulsoup/

## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/beautifulsoup-tutorial.git
$ cd beautifulsoup-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/beautifulsoup-tutorial.git
$ cd beautifulsoup-tutorial
$ pipenv shell
$ pipenv update
$ python3 main.py
```

**Installation via [Poetry](https://python-poetry.org/)**:

```shell
$ git clone https://github.com/hackersandslackers/beautifulsoup-tutorial.git
$ cd beautifulsoup-tutorial
$ poetry shell
$ poetry update
$ poetry run
```

## How to Use

This script will output metadata scraped from whichever URL is specified in **config.py**. Simply change the value of this variable to test the script against any URL of your choice.

------------------

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
