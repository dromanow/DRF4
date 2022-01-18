"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authors.views import AuthorModelViewSet, BioModelViewSet, BookModelViewSet
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='v1',
        description='',
        contact=openapi.Contact(email='test@test.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('bios', BioModelViewSet)
router.register('books', BookModelViewSet)

#  /authors/   GET, POST
#  /authors/1/ GET, PUT/PATCH, DELETE

# http://127.0.0.1:8000/api/authors/?name=Федор


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', TemplateView.as_view(template_name='index.html')),

    # re_path(r'^api/(?P<version>.\d)', AuthorModelViewSet.as_view({'get': 'list'})),
    # path('api/authors/v1', include('authors.urls', namespace='v1')),
    # path('api/authors/v2', include('authors.urls', namespace='v2'))

    # path('api/get/<str:name>', AuthorViewSet.as_view({'get': 'list'})),
    # path('api/get/<int:pk>/', AuthorAPIView.as_view()),

    # {'get': 'list'}
    # path('api/post/', post_view)
]
