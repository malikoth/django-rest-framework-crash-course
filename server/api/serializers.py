from rest_framework import serializers

from api import models


class BookSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='name', queryset=models.Tag.objects.all(), many=True)
    publisher = serializers.SlugRelatedField(slug_field='name', queryset=models.Publisher.objects.all())

    class Meta:
        model = models.Book


class TagSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(slug_field='name', queryset=models.Book.objects.all(), many=True)

    class Meta:
        model = models.Tag


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
