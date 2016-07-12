from rest_framework import serializers

from api import models, fields


class BookSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Tag.objects.all(),
        many=True)
    publisher = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Publisher.objects.all())
    authors = fields.DelimitedStringRelatedField(
        delimiter=' ',
        attribute_names=('first_name', 'last_name'),
        queryset=models.Person.objects.all(),
        many=True)

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
    name = fields.DelimitedStringRelatedField(
        delimiter=' ',
        attribute_names=('first_name', 'last_name'),
        queryset=models.Person.objects.all())

    class Meta:
        model = models.Person
        fields = ('id', 'name')
