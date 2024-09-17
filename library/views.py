from django.shortcuts import render
from rest_framework.filters import SearchFilter
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
    pagination_class = BooksPaginator
    filter_backends = [SearchFilter,]


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
