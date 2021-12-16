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
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorModelViewSet, BioModelViewSet, BookModelViewSet


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
    # path('api/get/<str:name>', AuthorViewSet.as_view({'get': 'list'})),
    # path('api/get/<int:pk>/', AuthorAPIView.as_view()),

    # {'get': 'list'}
    # path('api/post/', post_view)
#     я вот чет немного потерялся.. почему обращение к параметрам класса идет как обращение к параметрам инстанса? class UserViewSet(ModelViewSet): queryset = User.objects.all() def get_queryset(self,request): q = self.queryset # <- вот тут например. по идее же должно быть что-то в духе self.__cls__.queryset или UserViewSet.queryset где я что упускаю?
]
