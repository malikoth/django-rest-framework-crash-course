name: inverse
layout: true
class: center, middle, inverse

.left-column[

]
.right-column[

]


---

# Django REST Framework Crash Course

.footnote[
Follow along at https://git.io/drfcc
]

---

layout: false

.left-column[
## Overview

]
.right-column.large[
* Django
* REST and RESTful web APIs


* Serializing / deserializing data
* Representing data relationships
* Grouping functionality in viewsets
* Automatic endpoints with routers
]

---

template: inverse
# Django

---

.left-column[
## Django
### - Overview
]
.right-column.large[
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
.right-column.large[

.pull-left[
* Authentication
* Caching
* Logging
* Sending emails
* Syndication feeds (RSS / Atom)
* Pagination
* Messages framework
]
.pull-right[
* Serialization
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

template: inverse
# REST and RESTful web APIs

---

.left-column[
## REST
### - What is REST?
]
.right-column.large[
REpresentational State Transfer (REST) is an architectural style that describes six constraints.

To the extent that systems conform to the constraints of REST they can be called RESTful.
]

---

.left-column[
## REST
### - What is REST?
### - Constraints
]
.right-column.large[
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
.right-column.large[
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
.right-column.large[
* Resource (noun) based
* Use standard HTTP verbs to specify actions
* Use HTTP response codes to indicate status
* Offer responses in multiple formats (JSON, XML, etc.)
]

---

template: inverse
# Putting it all together

---

.left-column[
## Case Study: BetterReads
]
.right-column.large[
* Relationships
* Model definitions
* What it looks like
* Calling our API from a client
]

---

.left-column[
## Resources
]
.right-column.large[
* [REST API Tutorial](http://www.restapitutorial.com/)
]

---

.left-column[
## Sources
]
.right-column.large[
* [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) on Wikipedia
]
