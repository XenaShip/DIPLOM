from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from library.models import Books, Author
from library.pagination import BooksPaginator, AuthorPaginator
from library.serializer import BooksSerializer, AuthorSerializer


class BooksCreateApiView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksListApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # pagination_class = BooksPaginator
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ('name', 'availability', 'genre', 'user', 'author')
    # ordering_fields = ('name',)

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.all())
        if self.request.query_params.get('genre'):
            queryset = queryset.filter(genre=str(self.request.query_params.get('genre')))
            print('cool', queryset.all())
        return queryset


class BooksRetrieveApiView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksUpdateApiView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDestroyApiView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPaginator
    filter_backends = [SearchFilter, ]


class AuthorRetrieveApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksSearchApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

