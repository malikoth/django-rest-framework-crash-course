name: inverse
layout: true
class: center, middle, inverse

.left-column[

]
.right-column[

]


---

# Django REST Framework Crash Course

---

layout: false

.right-column[
# Overview
* Django
* REST and RESTful web APIs
* Serializing / deserializing data
* Representing data relationships
* Grouping functionality in viewsets
* Automatically creating endpoints with routers
]

---

template: inverse
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

> "With Django, you can take Web applications from concept to launch in a matter of hours. Django takes care of much of
the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and
open source."
]

---

.left-column[
## Django
### - Overview
### - Common Tools
]
.right-column[
* Authentication
* Caching
* Logging
* Sending emails
* Syndication feeds (RSS / Atom)
* Pagination
* Messages framework
* Serialization
* Sessions
* Sitemaps
* Statis files management
* Data validation
* Templating (DTL, Jinja2, etc.)
* Flatpages
* Redirects
]

---

template: inverse
# REST and RESTful web APIs

---

.left-column[
## REST
### - What is REST?
]
.right-column[
> "The REST architectural style describes six constraints. These constraints, applied to the architecture, were
originally communicated by Roy Fielding in his
[doctoral dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) and defines the basis of
RESTful-style."
]

---

.left-column[
## REST
### - What is REST?
### - Constraints
]
.right-column[
* Uniform Interface
* Stateless
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

template: inverse
# Putting it all together

---

.right-column[
# Case Study: BetterReads
* Relationships
* Model definitions
* What it looks like
* Calling our API from a client
]

---

.right-column[
# Resources
* [REST API Tutorial](http://www.restapitutorial.com/)
]