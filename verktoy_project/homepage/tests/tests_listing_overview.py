from django.test import TestCase
from homepage.models import Listing
from users.models import User

class ListingOverview(TestCase):

    def setUpTestData():
        user1 = User.objects.create_user(username="testuser1", password="password1")
        user2 = User.objects.create_user(username="testuser2", password="password2")
        user3 = User.objects.create_user(username="testuser3", password="password3")
        user4 = User.objects.create_user(username="testuser4", password="password4")
        listing1 = Listing.objects.create(  owner=user1,
                                            title="Sag", 
                                            loaned=True, 
                                            location="Trondheim", 
                                            description="Mye brukt", 
                                            category=4)

        listing2 = Listing.objects.create(  owner=user2,
                                            title="Skrujern", 
                                            loaned=False, 
                                            location="Oslo", 
                                            description="Pent brukt", 
                                            category=5)

        listing3 = Listing.objects.create(  owner=user3,
                                            title="Hammer", 
                                            loaned=True, 
                                            location="Bergen", 
                                            description="Dårlig håndtak", 
                                            category=1)

        listing4 = Listing.objects.create(  owner=user4,
                                            title="Skrumaskin", 
                                            loaned=False, 
                                            location="Stavanger", 
                                            description="Noen skraper", 
                                            category=3)

    def test_listingOverview(self):

        self.assertEqual(4, Listing.objects.count())

    def test_deleteListingFromOverview(self):

        listing4 = Listing.objects.get(id=4)

        self.assertEqual(4, Listing.objects.count())
        listing4.delete()
        self.assertEqual(3, Listing.objects.count())

    def test_addListingToOverview(self):
        
        self.assertEqual(4, Listing.objects.count())

        user2 = User.objects.get(id=2)
        counter = 0
        for listing in Listing.objects.all():
            if listing.owner == user2:
                counter += 1
        
        self.assertEqual(1, counter)

        listing5 = Listing.objects.create(  owner=user2,
                                            title="Tang", 
                                            loaned=True, 
                                            location="Stavanger", 
                                            description="Mange skraper", 
                                            category=4)
        self.assertEqual(5, Listing.objects.count())

        counter = 0
        for listing in Listing.objects.all():
            if listing.owner == user2:
                counter += 1
        
        self.assertEqual(2, counter)

    def test_getListingFromOverview(self):
        self.assertEqual("Sag", Listing.objects.get(id=1).title)
        self.assertFalse(Listing.objects.get(id=2).loaned)
        self.assertTrue(Listing.objects.get(id=3).loaned)
        self.assertEqual("Noen skraper", Listing.objects.get(id=4).description)





        
