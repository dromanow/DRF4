import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer, CharField, IntegerField, ValidationError
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, BasePermission
from .serializers import AuthorModelSerializer, BioModelSerializer, BookModelSerializer, AuthorModelSerializerV2
from .models import Author, Bio, Book


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [CustomPermission]
    queryset = Author.objects.all()
    # serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AuthorModelSerializerV2
        return AuthorModelSerializer


class BioModelViewSet(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


# class AuthorAPIView(APIView):
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request):
#         bio = Author.objects.get(pk=1)
#         serializer = AuthorModelSerializer(bio)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def author_view(request):
#     bio = Author.objects.get(pk=1)
#     serializer = AuthorModelSerializer(bio)
#     return Response(serializer.data)


class AuthorAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # def get(self, request):
    #     bio = Author.objects.get(pk=1)
    #     serializer = AuthorModelSerializer(bio)
    #     return Response(serializer.data)


class Pagination(LimitOffsetPagination):
    default_limit = 1


class AuthorViewSet(ListModelMixin, DestroyModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name']
    # pagination_class = Pagination

    @action(methods=['GET'], detail=True)
    def get_author_name(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        return Response({'name': str(author)})

    # def get_queryset(self):
    #     if 'name' in self.request.query_params:
    #         return Author.objects.filter(first_name=self.request.query_params.get('name'))
    #     return Author.objects.all()


# def perform_destroy(self, instance):
    #     instance.is_active = True
    #     instance.save()
    #     super().perform_destroy(instance)

    # def list(self, request):
    #     authors = Author.objects.all()
    #     serializer = AuthorModelSerializer(authors, many=True)
    #     return Response(serializer.data)


#  [Client] -> [Router/URL] -> [View] -> [Serializer] -> [Model]

# class AuthorSerializer(Serializer):
#     first_name = CharField(max_length=64)
#     last_name = CharField(max_length=64)
#     birthday_year = IntegerField()
#
#     def validate_birthday_year(self, value):
#         if value < 1000:
#             raise ValidationError('Value mut be gt 1000')
#         return value
#
#     def validate(self, attrs):
#         if attrs['last_name'] == '??????????????????????' and attrs['birthday_year'] != 1821:
#             raise ValidationError('birthday_year must be 1821')
#         return attrs
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         author = Author(**validated_data)
#         author.save()
#         return author
#
#
# class BioSerializer(Serializer):
#     text = CharField(max_length=64)
#     author = AuthorSerializer()
#
#
# class BookSerializer(Serializer):
#     text = CharField(max_length=64)
#     authors = AuthorSerializer(many=True)
#

# def get_view(request):
#     bio = Book.objects.get(pk=1)
#     serializer = BookSerializer(bio)
#     render = JSONRenderer()
#     json_data = render.render(serializer.data)
#     print(serializer.data)
#     return HttpResponse(json_data)

#
#     # author = Author.objects.get(pk=1)
#     # serializer = AuthorSerializer(author)
#     # render = JSONRenderer()
#     # json_data = render.render(serializer.data)
#     # print(serializer.data)
#     # return HttpResponse(json_data)

#
# @csrf_exempt
# def post_view(request):
#     print(request.body)
#     data = JSONParser().parse(io.BytesIO(request.body))
#
#     if request.method == 'POST':
#         serializer = AuthorSerializer(data=data)
#     elif request.method == 'PUT':
#         author = Author.objects.get(pk=3)
#         serializer = AuthorSerializer(author, data=data)
#     elif request.method == 'PATCH':
#         author = Author.objects.get(pk=3)
#         serializer = AuthorSerializer(author, data=data, partial=True)
#
#     if serializer.is_valid():
#         print(serializer.validated_data)
#
#         author = serializer.save()
#         serializer = AuthorSerializer(author)
#         render = JSONRenderer()
#         json_data = render.render(serializer.data)
#         print(serializer.data)
#         return HttpResponse(json_data)
#     else:
#         return HttpResponseServerError(serializer.errors['non_field_errors'])
