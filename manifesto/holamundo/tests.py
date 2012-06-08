"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_load_template(self):
    	#Arrange
        response = self.client.get("/")
        #Assert
        self.assertTemplateUsed(response,'holamundo.html')