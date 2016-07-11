from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Person, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books')
    publisher = models.ForeignKey(Publisher, null=True)
