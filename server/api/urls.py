from django.conf.urls import include, url

from rest_framework import routers

from api import views

api = routers.DefaultRouter()
api.register('books', views.BookViewSet)
api.register('tags', views.TagViewSet)
api.register('publishers', views.PublisherViewSet)
api.register('people', views.PersonViewSet)

urlpatterns = [
    url(r'^', include(api.urls))
]
