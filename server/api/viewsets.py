from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response


class SelfDescribingModelViewSet(viewsets.ModelViewSet):
    def strip_querysets(self, field):
        for kwarg, value in list(field._kwargs.items()):
            if kwarg == 'queryset':
                del field._kwargs[kwarg]
            if hasattr(value, '_kwargs'):
                field = self.strip_querysets(value)
        return field

    @list_route(methods=['get'])
    def metadata(self, request):
        serializer = self.serializer_class()
        fields = serializer.get_fields()
        data = {name: str(self.strip_querysets(field)) for name, field in fields.items()}
        return Response(data, status=status.HTTP_200_OK)
