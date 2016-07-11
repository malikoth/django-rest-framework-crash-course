from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers, viewsets

from api import views
from api import utility


api = routers.DefaultRouter()
for attribute_name in dir(views):
    view = getattr(views, attribute_name)
    try:
        if issubclass(view, viewsets.GenericViewSet):
            view_name = utility.pluralize(view.serializer_class.Meta.model.__name__).lower()
            api.register(view_name, view)
    except:
        continue

urlpatterns = [
    url(r'^', include(api.urls)),
    url(r'^admin/', admin.site.urls),
]
