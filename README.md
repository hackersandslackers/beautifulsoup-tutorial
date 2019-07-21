# Linkbox API

![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.0.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-v4.6.3-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/linkbox-api.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/toddbirchard/linkbox-api/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/linkbox-api.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/toddbirchard/linkbox-api/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/linkbox-api.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/toddbirchard/linkbox-api/network)

**Linkbox** is a single endpoint which accepts a `?url=` parameter and returns best-guess metadata for the target site. A successfully executed request will parse the HTML of the target page and derive a link preview. The resulting JSON can be used to format embedded HTML previews, thereby creating a better visual experience as well as countless SEO benefits.

![Link Preview](https://raw.githubusercontent.com/toddbirchard/linkbox-api/master/img/linkboxgithub.jpg)

## Usage

![Link Preview](https://raw.githubusercontent.com/toddbirchard/linkbox-api/master/img/linkboxdemo.gif)

## Features in Development

There are several major features which remain in development:

* **AI-Generated Summaries**: Get the best synopsis of an article or webpage possible by letting robots write them for you.
* **Returning Embed HTML**: Instead of simply returning JSON containing metadata per request, users will be able to opt in to instead receiving a text response of HTML for an embedded widget.
* **Customized Responses**: Some content providers (such as Medium) are intentionally resistant to scrapers. Exceptions for such sources will be handled on a case-by-case basis to ensure meaningful data is returned.
* **Content Awareness**: Depending on the content of the link, a different embed will be returned to best display said content.
* **Direct Database Writes**: Integration with a site's content database to ensure HTML is hard-embedded to the page as opposed to a client-side script.
