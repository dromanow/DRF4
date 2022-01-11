from django.urls import path
from .views import AuthorModelViewSet

app_name = 'authors'

urlpatterns = [
    path(r'', AuthorModelViewSet.as_view({'get': 'list'}))
]
