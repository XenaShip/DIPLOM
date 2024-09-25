# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from library.models import Books, Author
# from users.models import User
#
#
# class SomeTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(email='test@yandex.ru', password='12345')
#         self.client.login(email='test@yandex.ru', password='12345')
#
#         refresh = RefreshToken.for_user(self.user)
#         self.access_token = str(refresh.access_token)
#
#     def test_create_book(self):
#         author = Author.objects.create(name='Cool')
#         data = {
#             'name': 'Cook',
#             'availability': True,
#             'genre': 'Cool',
#             'author': author.pk
#         }
#         response = self.client.post(
#             '/library/books/create/',
#             data=data
#         )
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#     def test_books_list(self):
#         author = Author.objects.create(name='Cool')
#         data = {
#             'name': 'Готовка',
#             'availability': True,
#             'genre': 'Развлечения',
#             'author': author.id
#         }
#         response = self.client.get(
#             '/library/books/'
#         )
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#

