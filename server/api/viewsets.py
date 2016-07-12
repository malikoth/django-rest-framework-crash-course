from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response


class SelfDescribingModelViewSet(viewsets.ModelViewSet):
    @list_route(methods=['get'])
    def metadata(self, request):
        serializer = self.serializer_class()
        fields = serializer.get_fields()
        data = {name: hasattr(field, 'child_relation') for name, field in fields.items()}
        return Response(data, status=status.HTTP_200_OK)
