from rest_framework import viewsets

import api.viewsets
from api import models
from api import serializers


class BookViewSet(api.viewsets.SelfDescribingModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
