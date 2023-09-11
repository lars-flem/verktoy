from django.test import TestCase
from homepage.models import Listing
from users.models import User

class ListingEdit(TestCase):
    
    def setUpTestData():
        user1 = User.objects.create_user(username="testuser1", password="password1")
        user2 = User.objects.create_user(username="testuser2", password="password2")

        Listing.objects.create(  owner=user1,
                                 title="Sag", 
                                 loaned= False, 
                                 location="Trondheim", 
                                 description="Mye brukt", 
                                 category=4)
        
        Listing.objects.create(  owner=user2,
                                 title="Skrujern", 
                                 loaned=False, 
                                 location="Oslo", 
                                 description="Pent brukt", 
                                 category=5)
        
    def test_editListing(self):
        listing1 = Listing.objects.get(id=1)
        self.assertEqual("Sag", listing1.title)
        listing1.title = "Hammer"
        self.assertEqual("Hammer", listing1.title)

        listing2 = Listing.objects.get(id=2)
        self.assertEqual("Pent brukt", listing2.description)
        listing2.description = "Lite brukt"
        self.assertEqual("Lite brukt", listing2.description)

    def test_removeListing(self):
        self.assertEqual(2, Listing.objects.count())
        listing2 = Listing.objects.get(id=2)
        listing2.delete()
        self.assertEqual(1, Listing.objects.count())