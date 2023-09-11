from django.db import IntegrityError
from django.test import TestCase
from homepage.models import Listing
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your tests here.

class UserTest(TestCase):

    def test_createUser(self):
        user1 = User.objects.create_user(username="OlaNordmann", password="jeglikerkoding")
        user2 = User.objects.create_user(username="JensMuri", password="gløshaugen")
        self.assertEqual("OlaNordmann", user1.username)
        self.assertEqual("JensMuri", user2.username)

    def test_createSameUserButDiffPassword(self):
        user1 = User.objects.create_user(username="OlaNordmann", password="jeglikerkoding")
        try:
            user2 = User.objects.create_user(username="OlaNordmann", password="jeglikerkoding")
            self.fail
        except IntegrityError:
            pass