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

![Link Preview](https://github.com/toddbirchard/linkbox/blob/master/img/linkboxgithub.jpg?raw=true)

## Usage

Public access coming soon!

**Request:**

```
curl https://linkbox.link?url=https://www.theatlantic.com/magazine/archive/2018/05/barbara-ehrenreich-natural-causes/556859/
```

**Response:**
```
{
  "author": "Victoria Sweet",
  "feeds": ["https://www.theatlantic.com/feed/all/",
    "https://www.theatlantic.com/feed/best-of/"
  ],
  "image": "https://cdn.theatlantic.com/assets/media/img/2018/04/_BarbaraEhrenreich_FINAL_RVB/facebook.png?1523295067",
  "postOrigin": "https://hackersandslackers.com/lynx-roundup-april-22nd",
  "publishDate": "2018-04-10T08:00:00+00:00",
  "summary": "I went to medical school, at least in part, to get to know death and perhaps to make my peace with it. One day—usually when you’re young, though sometimes later—the thought hits you: You really are going to die. Meanwhile, I watched as what had been called “medical care”—that is, treating the sick—turned into “health care,” keeping people healthy, at an ever-rising cost.",
  "tags": ["control",
    "cancer cells",
    "delays death",
    "ever-rising cost",
    "spiritual epiphanies",
    "strong family history",
    "firsthand experience",
    "fast-growing literature",
    "regular physical exams",
    "Natural Causes",
    "finally unevadable death",
    "new science",
    "immune system—and",
    "immediate health-care costs",
    "chronicling cultural shifts",
    "congenial new home",
    "popular delusions",
    "white blood cell"
  ],
  "title": "Your Body Is a Teeming Battleground",
  "url": "https://www.theatlantic.com/magazine/archive/2018/05/barbara-ehrenreich-natural-causes/556859/",
  "videos": []
}
```

## Functionality in Development

There are several major features which remain in development:

* **Returning Embed HTML**: Instead of simply returning JSON containing metadata per request, users will be able to opt in to instead receiving a text response of HTML for an embedded widget.
* **Customized Responses**: Some content providers (such as Medium) are intentionally resistant to scrapers. Exceptions for such sources will be handled on a case-by-case basis to ensure meaningful data is returned.
* **Content Awareness**: Depending on the content of the link, a different embed will be returned to best display said content.
* **Direct Database Writes**: Integration with a site's content database to ensure HTML is hard-embedded to the page as opposed to a client-side script.
