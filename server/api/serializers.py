from rest_framework import serializers

from api import models


class BookSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Tag.objects.all(),
        many=True)
    publisher = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Publisher.objects.all(),
        allow_null=True)
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = models.Book


class TagSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Book.objects.all(),
        many=True)

    class Meta:
        model = models.Tag


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher


class PersonSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = models.Person
