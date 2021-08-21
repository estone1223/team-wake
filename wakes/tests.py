from wakes.models import Wake
from django.http import response
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your tests here.

# class CreateWakeTest(TestCase):
#     def setUp(self):
#         self.user = UserModel.objects.create(
#             username = "test_user",
#             password = "secret",
#         )
#         self.client.force_login(self.user)

#     def test_render_creation_form(self):
#         response = self.client.get('/wakes/new/')
#         self.assertContains(response, 'Wakeの登録', status_code=200)

#     def test_create_wake(self):
#         data = {'name': 'test', 'description': 'test dayo'}
#         self.client.post('wakes/new/', data)
#         wake = Wake.objects.get(name='test')
#         self.assertEqual('test', wake.name)
#         self.assertEqual('test dayo', wake.description)