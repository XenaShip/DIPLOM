from django.contrib.auth.decorators import permission_required
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from library.models import Books, Author
from library.permissions import IsLibrarian
from users.models import User
from django.contrib.auth.models import Group


class SomeTestCase(APITestCase):

    def setUp(self):
        # self.user = User.objects.get(email='admin@sky.pro')
        self.user = User.objects.create(email='test@yandex.ru', password='12345')
        group = Group.objects.get(name='Librarian')
        self.user.groups.add(group)
        # self.user.user_permissions.set(['library.add_author',
        #                             'library.change_author',
        #                             'library.delete_author',
        #                             'library.view_author',
        #                             'library.add_books',
        #                             'library.change_books',
        #                             'library.delete_books',
        #                             'library.view_books',
        #                             ])
        self.client.login(email='test@yandex.ru', password='12345')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_create_book(self):
        author = Author.objects.create(name='Cool')
        data = {
            'name': 'Cook',
            'availability': True,
            'genre': 'Cool',
            'author': author.pk
        }
        response = self.client.post(
            '/library/books/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_books_list(self):
        response = self.client.get(
            '/library/books/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

