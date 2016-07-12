from rest_framework.relations import RelatedField


class DelimitedStringRelatedField(RelatedField):
    def __init__(self, *args, **kwargs):
        self.attribute_names = kwargs.pop('attribute_names')
        self.delimiter = kwargs.pop('delimiter', ',')
        if not self.attribute_names:
            raise Exception('At leaset one attribute name is required')
        super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        return instance

    def to_representation(self, obj):
        return self.delimiter.join(getattr(obj, attribute) for attribute in self.attribute_names)

    def to_internal_value(self, data):
        attributes = dict(zip(self.attribute_names, data.split(self.delimiter)))
        return self.get_queryset().get(**attributes)
