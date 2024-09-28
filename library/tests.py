from django.contrib.auth.decorators import permission_required
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from library.models import Books, Author
from library.permissions import IsLibrarian
from users.models import User
from django.contrib.auth.models import Group, Permission


class SomeTestCase(APITestCase):

    def setUp(self):
        # self.user = User.objects.get(email='admin@sky.pro')
        self.user = User.objects.create(email='test@yandex.ru', password='12345')
        self.special_group = Group.objects.create(name='Librarian')
        self.user.groups.add(self.special_group)
        print("test_setUp")
        # perm = Permission.objects.get(codename='library.add_author')
        #self.user.user_permissions.add(perm)
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
        self.client.force_authenticate(user=self.user)

    def test_create_author(self):
        response = self.client.post(
            '/library/author/create/',
            data={'name': 'Cool', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_author(self):
        author = Author.objects.create(name='Cool')
        response = self.client.patch(
            f'/library/author/{author.pk}/update',
            data={'name': 'Bad', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_create_book(self):
        author = Author.objects.create(name='Cool')
        data = {
             'name': 'Cook',
             'availability': True,
             'genre': 'Hard',
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

    def test_books_update(self):
        author = Author.objects.create(name='Cool')
        book = Books.objects.create(name='Cook', availability=True, genre='Hard', author=author)
        response = self.client.patch(
            f'/library/books/{book.pk}/update',
            data={'name': 'Bad',}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_author_delete(self):
        author = Author.objects.create(name='Cool')
        response = self.client.delete(
            f'/library/author/{author.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_book_delete(self):
        author = Author.objects.create(name='Cool')
        book = Books.objects.create(name='Cook', availability=True, genre='Hard', author=author)
        response = self.client.delete(
            f'/library/books/{book.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_books_list(self):
        author = Author.objects.create(name='Cool')
        book = Books.objects.create(name='Cook', availability=True, genre='Hard', author=author)
        response = self.client.get(
            '/library/books/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_authors_list(self):
        author = Author.objects.create(name='Cool')
        response = self.client.get(
            '/library/author/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_create(self):
        response = self.client.post(
            '/users/register/',
            data={'name': 'Cool', 'email': 'j@yandex.ru', 'password': '123'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_user(self):
        user = User.objects.create(name='Cool', email='j@yandex.ru', password='123')
        response = self.client.patch(
            f'/users/user/{user.pk}/update',
            data={'name': 'Bad', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_user_delete(self):
        user = User.objects.create(name='Cool', email='j@yandex.ru', password='123')
        response = self.client.delete(
            f'/users/user/{user.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
    def test_user_list(self):
        user = User.objects.create(name='Cool', email='j@yandex.ru', password='123')
        response = self.client.get(
            '/users/user/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )



