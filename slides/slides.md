name: title
layout: true
class: center, middle, huge
background-image: url('blue-wallpaper.jpg')

.left-column[

]
.right-column[

]

---

name: background
layout: true
background-image: url('blue-wallpaper.jpg')

---

template: title
# Django REST Framework Crash Course
### Kyle Rich

.footnote[
Follow along at https://git.io/drfcc
]

---

.left-column[
## Overview
### - Quick Introductions
]
.right-column[
* Django
* REST and RESTful web APIs
* Example project
]

---

.left-column[
## Overview
### - Quick Introductions
### - Django REST Framework
]
.right-column[
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
* Resource (noun) based, collections and instances
* Use standard HTTP verbs to specify actions
* Use HTTP response codes to indicate status
* Offer responses in multiple formats (JSON, XML, etc.)
]

---

template: title
# Example Project:
# &nbsp;
???

I love reading, and I use GoodReads to make it a somewhat social experience.  But GoodReads isn't perfect.  It could be
better.  Better than good.  So I decided to start work on...

--
BetterReads

???

...BetterReads!  Which will be better than GoodReads!

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

???

Note that the serializer knows the model class, and it knows all of the attributes on that class.  The ModelSerializer
default behavior automatically creates an appropriate serializer field for each attribute on the model

--

.right-column[
```json
{
  'address': '12345 S. State Street',
  'id': 1,
  'name': 'Del Rey'
}
```
]

---

.left-column[
## Serialization
### - Publisher
### - Person
]
.right-column[
```python
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        unique_together = ('first_name', 'last_name')
```
]

???

The unique_together constraint creates a multi-column index keeping all combinations of first and last names unique.

--

.right-column[
```python
class PersonSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = models.Person
```
]

???

We can customize the way the email field is serialized by giving it a different serializer field.  The EmailField
serializer will check for a valid e-mail address before accepting the input.

---

.left-column[
## Serialization
### - Publisher
### - Person
### - Tag
]
.right-column[
```python
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
```
]
--

.right-column[
```python
class TagSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(
        slug_field='name', many=True
        queryset=models.Book.objects.all())

    class Meta:
        model = models.Tag
```
]

???

The slug related field alters the way a data relationship is displayed, by simply displaying one of the attributes
of the related object.  The attribute it shows is specified in the slug_field.

---

.left-column[
## Serialization
### - Publisher
### - Person
### - Tag
### - Book
]
.right-column[
```python
class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Person)
    tags = models.ManyToManyField(Tag)
    publisher = models.ForeignKey(Publisher, null=True)
    year = models.IntegerField(null=True)
    in_print = models.BooleanField(default=True)
```
]
--

.right-column[
```python
class BookSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name', many=True,
        queryset=models.Tag.objects.all())
    publisher = serializers.SlugRelatedField(
        slug_field='name', allow_null=True,
        queryset=models.Publisher.objects.all())
    url = serializers.HyperlinkedIdentityField(
        view_name='book-detail')

    class Meta:
        model = models.Book
```
]

???

The HyperlinkedIdentityField creates a link to the current object's representation.  The url field is automatically
created with the same field serializer if you subclass HyperlinkedModelSerializer instead of ModelSerializer.

---

.left-column[
## Serialization
### - Publisher
### - Person
### - Tag
### - Book
### - Book JSON
]
.right-column[
```json
{
  'authors': [
    1
  ],
  'id': 1,
  'in_print': True,
  'name': 'A Really Good Book',
  'publisher': None,
  'tags': [
    'Fun',
    'Fantasy'
  ],
  'url': 'http://localhost:8000/api/books/1/',
  'year': 2016
}
```
]

???

Note that authors and tags are both M2M relationships, but they render differently.  Is anyone surprised by this?

---


.left-column[
## Serialization
### - Publisher
### - Person
### - Tag
### - Book
### - Book JSON
### - Notes
]
.right-column[
* Serializers render Python objects to plain-text representation (JSON, XML, etc.)
]
--

.right-column[
* They also parse plain-text representations (JSON, XML, etc.) and convert back to Python objects
]
--

.right-column[
* You can control and override how both of those processes work
]
--

.right-column[
* Serializer classes give you broad control
]
--

.right-column[
* Serializer fields give you granular control
]

---

template: title
# ViewSets

---

.left-column[
## ViewSets
### - Methods
]
.right-column[
We're used to talking in terms of HTTP methods
* GET
* POST
* PUT
* PATCH
* DELETE
* OPTIONS
* HEAD
]

---

.left-column[
## ViewSets
### - Methods
### - Actions
]
.right-column[
DRF talks in terms of "actions"
* list
* create
* retrieve
* update
* delete
]

---

.left-column[
## ViewSets
### - Methods
### - Actions
### - Detail View
]
.right-column[
Detail view is for actions on an instance, or in other words, any time you have the primary key.

```
/api/books/1/
```

* GET -> retrieve
* PUT / PATCH -> update
* DELETE -> delete
]

---

.left-column[
## ViewSets
### - Methods
### - Actions
### - Detail View
### - List View
]
.right-column[
List view is for actions when you don't have a primary key.

```
/api/books/
```

* GET -> list
* POST -> create
]

---

.left-column[
## ViewSets
### - Methods
### - Actions
### - Detail View
### - List View
### - Grouping
]
.right-column[
DRF will happily create a view for every action you need with ViewSets.

```python
class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
```
]
--

.right-column.padding[
TagViewSet and PublisherViewSet are virtually identical to PersonViewSet.
]

---

.left-column[
## ViewSets
### - Methods
### - Actions
### - Detail View
### - List View
### - Grouping
### - Filtering
]
.right-column[
Here's the most interesting thing my viewsets do:

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_fields = ('year', 'in_print', 'authors',
                     'name', 'tags', 'publisher')
```
]

???

Note that the ModelViewSet creates all five actions, but there are other viewsets that only create the actions for a read-only
resource, or you can mix and match them to get the required functionality for a resource.

---

template: title
# Routers

---

.left-column[
## Routers
### - Review
]
.right-column[
* Models created with Django ORM
]
--

.right-column[
* Object serialized to representation in desired format
]
--

.right-column[
* Viewsets to interact with each resource
]
--

.right-column[
# What are we still missing?
]

---

.left-column[
## Routers
### - Review
### - URLs
]
.right-column[
```python
from django.conf.urls import include, url

from rest_framework import routers

from api import views

api = routers.DefaultRouter()
api.register('books', views.BookViewSet)
api.register('tags', views.TagViewSet)
api.register('publishers', views.PublisherViewSet)
api.register('people', views.PersonViewSet)

urlpatterns = [
    url(r'^', include(api.urls))
]

```
]

---

template: title
# Let's play with it!

---

.left-column[
# Let's play with it!
]
.right-column.no-curves[
```python
Python 3.5.1 (default, Dec  7 2015, 21:59:08)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0
(clang-700.1.76)] on darwin
Type "help", "copyright", "credits" or
"license" for more information.
```
]
--

.right-column.no-padding.no-curves[
```python
>>> import requests
```
]
--

.right-column.no-padding.no-curves[
```python
>>> from pprint import pprint
```
]
--

.right-column.no-padding.no-curves[
```python
>>> data = requests.get(
...     'http://localhost:8000/api/people/'
... ).json()
```
]
--

.right-column.no-padding.no-curves[
```python
>>> pprint(data)
[{'email': 'kyle@mydomain.com',
  'first_name': 'Kyle',
  'id': 1,
  'last_name': 'Rich'}]
```
]

???

If there's time, open up the console and play with the client I made.

---

template: title
# Questions?

---

.left-column[
## Resources
]
.right-column[
* This talk https://git.io/drfcc
* REST API Tutorial http://www.restapitutorial.com/
* [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) on Wikipedia
* Django REST Framework documentation http://www.django-rest-framework.org/
* RemarkJS Markdown based presentation framework http://remarkjs.com

## Please leave feedback!
https://joind.in/talk/40348
]
