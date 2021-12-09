import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorModelSerializer
from .models import Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


def get_view(request):
    pass


@csrf_exempt
def post_view(request):
    pass
