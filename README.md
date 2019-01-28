# Linkbox

![Python](https://img.shields.io/badge/Python-3.7.1-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![Flask](https://img.shields.io/badge/flask-1.0.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![BeautifulSoup](https://img.shields.io/badge/beautifulsoup4-4.6.3-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=36363e)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/linkbox.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/linkbox/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/linkbox.svg?style=flat-square&colorB=e3bb18&colorA=36363e)](https://github.com/toddbirchard/linkbox/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/linkbox.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/Link-Preview-API/network)

**Linkbox** is a single endpoint which accepts a `?url=` parameter and returns best-guess metadata for the target site. A successful request parses HTML of the target page and discerns which data is best suited to provided a preview of said page. The resulting JSON can be used to format embedded HTML previews, thereby creating a better visual experience as well as countless SEO benefits.

Public access coming soon!

![Link Preview](https://github.com/toddbirchard/linkbox/blob/single/img/linkbox-terminal.png)

## Usage

Request:

```
curl https://linkbox.link?url=https://venturebeat.com/2018/10/16/github-launches-actions-to-execute-code-in-containers-and-security-alerts-for-java-and-net-projects/
```

Response:
```
{
  "title": "GitHub launches Actions to execute code in containers and security alerts for Java and .NET projects | VentureBeat",
  "description": "GitHub introduced Actions for automated workflows and code execution in containers on GitHub, alongside other changes to the developer platform.",
  "image": "https://venturebeat.com/wp-content/uploads/2018/10/UPDATED-Actions-blog-screenshot-1.png?w=600",
  "sitename": "VentureBeat",
  "url": "https://venturebeat.com/2018/10/16/github-launches-actions-to-execute-code-in-containers-and-security-alerts-for-java-and-net-projects/"
}
```

## Functionality in Development

There are several major features which remain in development:

* **Returning Embed HTML**: Instead of simply returning JSON containing metadata per request, users will be able to opt in to instead receiving a text response of HTML for an embedded widget.
* **Customized Responses**: Some content providers (such as Medium) are intentionally resistant to scrapers. Exceptions for such sources will be handled on a case-by-case basis to ensure meaningful data is returned.
* **Content Awareness**: Depending on the content of the link, a different embed will be returned to best display said content.
* **Direct Database Writes**: Integration with a site's content database to ensure HTML is hard-embedded to the page as opposed to a client-side script.
