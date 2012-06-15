from django.contrib.auth.models import User
from signers.models import SignerProfile
from django.test.client import Client

from django.test import TestCase

# Falta hacer test
# class SimpleTest(TestCase):
#     def setUp(self):
#         response = self.client('/accounts/signup/', {'first_name': 'Nombre',
#                                                      'last_name': 'Apellido',
#                                                      'email': 'npinillac@gmail.com',
#                                                      'password1': '12345',
#                                                      'password2': '12345',
#                                                      })