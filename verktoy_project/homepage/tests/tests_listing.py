from django.forms import ValidationError
from django.test import TestCase
from homepage.models import Listing
from users.models import User

# Create your tests here.

class ListingTests(TestCase):
    def setUpTestData():
       User.objects.create_user(username="testuser", password="123")
       Listing.objects.create(  owner= User.objects.get(id=1), 
                                title="Skrujern", 
                                loaned=False, 
                                location="Oslo", 
                                description="Skrujern i god stand", 
                                category=4)

    def test_createListing(self):
        user = User.objects.get(id=1)
        listing = Listing.objects.create(  owner=user,
                                            title="Sag", 
                                            loaned=True, 
                                            location="Trondheim", 
                                            description="Mye brukt", 
                                            category=1)

        testUser = listing.owner
        self.assertEqual(user.username, testUser.username)
        self.assertEqual(user.password, testUser.password)

        self.assertEqual("Sag", listing.title)
        self.assertTrue(listing.loaned)
        self.assertEqual("Trondheim", listing.location)
        self.assertEqual("Mye brukt", listing.description)
        self.assertEqual(1, listing.category)

    def test_title(self):
        listing = Listing.objects.get(id=1)
        listing.title = "Hammer"
        self.assertEqual("Hammer", listing.title)
        listing.title = "Vater"
        self.assertEqual("Vater", listing.title)

    def test_loaned(self):
        listing = Listing.objects.get(id=1)
        listing.loaned = True
        self.assertTrue(listing.loaned)
        listing.loaned = False
        self.assertFalse(listing.loaned)
    
    def test_location(self):
        listing = Listing.objects.get(id=1)
        listing.location = "Oslo"
        self.assertEqual("Oslo", listing.location)
        listing.location = "Bergen"
        self.assertEqual("Bergen", listing.location)
    
    def test_description(self):
        listing = Listing.objects.get(id=1)
        listing.description = "Pent brukt verktøy"
        self.assertEqual("Pent brukt verktøy", listing.description)
        listing.description = "Helt ødelagt"
        self.assertEqual("Helt ødelagt", listing.description)

    def test_category(self):
        listing = Listing.objects.get(id=1)
        listing.category = 3
        self.assertEqual(3, listing.category)
        listing.category = 5
        self.assertEqual(5, listing.category)

    def test_errorLoaned(self):
        user = User.objects.get(id=1)
        try:
            listing = Listing.objects.create(  owner=user,
                                            title="Sag", 
                                            loaned="Utlånt", 
                                            location="Trondheim", 
                                            description="Mye brukt", 
                                            category=1)
            self.fail
        except ValidationError:
            pass