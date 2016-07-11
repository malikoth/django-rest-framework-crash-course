from rest_framework import serializers

from api import models


class BookSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name',
        allow_null=True,
        required=False,
        queryset=models.Tag.objects.all(),
        many=True)

    class Meta:
        model = models.Book


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
