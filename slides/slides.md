name: title
layout: true
class: center, middle, huge
background-image: url('http://wallpaperlayer.com/img/2015/7/cool-blue-textured-backgrounds-6923-7203-hd-wallpapers.jpg')

.left-column[

]
.right-column[

]

---

name: background
layout: true
background-image: url('http://wallpaperlayer.com/img/2015/7/cool-blue-textured-backgrounds-6923-7203-hd-wallpapers.jpg')

---

template: title
# Django REST Framework Crash Course

.footnote[
Follow along at https://git.io/drfcc
]

---

.left-column[
## Overview

]
.right-column[
## Quick introductions
* Django
* REST and RESTful web APIs
* Example project

## Django REST Framework
* Serializing / deserializing data
* Representing data relationships
* Grouping functionality in viewsets
* Automatic endpoints with routers
]

---

template: title
# Django

---

.left-column[
## Django
### - Overview
]
.right-column[
> "The web framework for perfectionists with deadlines."

> "Django was invented to meet fast-moving newsroom deadlines, while satisfying the tough requirements of experienced
Web developers."
]

---

.left-column[
## Django
### - Overview
### - Common Tools
]
.right-column[
.pull-left[
* Authentication
* Caching
* Logging
* Sending emails
* Syndication feeds (RSS / Atom)
* Pagination
* Messages framework
* Serialization
]
.pull-right[
* Sessions
* Sitemaps
* Static  files management
* Data validation
* Templating (DTL, Jinja2, etc.)
* Flatpages
* Redirects
]
]

---

template: title
# REST and RESTful web APIs

---

.left-column[
## REST
### - What is REST?
]
.right-column[
REpresentational State Transfer (REST) is an architectural style that describes six constraints.

To the extent that systems conform to the constraints of REST they can be called RESTful.
]

---

.left-column[
## REST
### - What is REST?
### - Constraints
]
.right-column[
* Uniform Interface
* Stateless (HATEOAS)
* Cacheable
* Client-Server
* Layered System
* Code on Demand (optional)
]

---

.left-column[
## REST
### - What is REST?
### - Constraints
### - What it buys us
]
.right-column[
* Performance
* Scalability
* Simplicity
* Modifiability
* Visibility
* Portability
* Reliability
]

---

.left-column[
## REST
### - What is REST?
### - Constraints
### - What it buys us
### - Web APIs
]
.right-column[
* Resource (noun) based
* Use standard HTTP verbs to specify actions
* Use HTTP response codes to indicate status
* Offer responses in multiple formats (JSON, XML, etc.)
]

---

template: title
# Example Project:
#&nbsp;
--
BetterReads

---

background-image: url('graph.png')

---

.left-column[
## Serialization
### - Publisher
]
.right-column[
```python
class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
```
]
--

.right-column[
```python
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
```
]

---

.left-column[
## Resources
]
.right-column[
* [REST API Tutorial](http://www.restapitutorial.com/)
]

---

.left-column[
## Sources
]
.right-column[
* [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) on Wikipedia
]
