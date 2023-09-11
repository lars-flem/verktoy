from django.test import TestCase
from homepage.models import Listing
from users.models import User
# Create your tests here.



class OwnListingsTest(TestCase):
    
    def test_own_listings(self):
        #en del kode, kunne hatt egen setup funksjon
        user1=User.objects.create_user(username="testuser1", password="123")
        User.objects.create_user(username="testuser2", password="123")
        Listing.objects.create(owner=User.objects.get(id=1),
                                title="listing 1",
                                loaned=False, 
                                location="test",
                                category=1)
        Listing.objects.create(owner=User.objects.get(id=1),
                                title="listing 2",
                                loaned=False, 
                                location="test",
                                category=1)
        Listing.objects.create(owner=User.objects.get(id=2),
                                title="listing 3",
                                loaned=False, 
                                location="test",
                                category=1)
        
        #Denne testen tester om det kun er dine egne listings som kommer opp på min bruker.
        #I .views ligger listen own_listings som er en liste med egne listings
        #Siden own_listings ligger i .views og ikke i .models, kan man ikke hente ut liste fra .models
        #Isteden har jeg laget en ny liste user1_own_listings, som er gjort på samme måte som i .views
        #Er litt tullete måte å teste på
        
        #samme linje kode som users/view
        user1_own_listings=Listing.objects.filter(id=1)
        for listing in user1_own_listings:
            self.assertEqual(user1.username, listing.owner.username)
            
