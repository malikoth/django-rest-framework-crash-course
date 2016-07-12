from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Person, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books')
    publisher = models.ForeignKey(Publisher, null=True, related_name='books')
    year = models.IntegerField(null=True)
    in_print = models.BooleanField(default=True)

    def __str__(self):
        return self.name
