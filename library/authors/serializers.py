from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Author


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'first_name']
