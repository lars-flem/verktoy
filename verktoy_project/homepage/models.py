from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.

#Klasse/modell for å annonser (Listings)
class Listing(models.Model):
    owner = models.ForeignKey(User, verbose_name = 'User', on_delete=models.CASCADE, null=True) #user burde kanskje endres til settings.AUTH_USER_MODEL. må i så fall django.conf import settings
    title = models.CharField(max_length=50, verbose_name="Tittel")
    image = models.ImageField(upload_to='images/', null=True)
    loaned = models.BooleanField(default=False, verbose_name="Utlånt?")
    price = models.PositiveSmallIntegerField(verbose_name='Pris', default=0)
    location = models.CharField(max_length=100, verbose_name="Sted") #burde kanskje være annet enn CharField. Gjør det vanskelig å sortere etter denne attributten
    description = models.TextField(verbose_name="Beskrivelse")

    #For under, se https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices.
    #Heltall for raskere sortering.
    SW = 1
    PT = 2
    WD = 3
    CT = 4
    SV = 5
    BO = 6
    OT = 7
    CATEGORY_CHOICES = (
        (SW, 'Saging'),
        (PT, 'Maling'),
        (WD, 'Sveising'),
        (CT, 'Kutt/Kapping'),
        (SV, 'Skruverktøy'),
        (BO, 'Slagverktøy'),
        (OT, 'Annet'),
    )
    category = models.PositiveSmallIntegerField(
        choices = CATEGORY_CHOICES,
        default = OT,
        verbose_name="Kategori",
    )

    def __str__(self):
        return self.title
    

class AgreementManager(models.Manager):
    def create_agreement(self, owner, loaner, listing):
        agreement =self.create(owner=owner, loaner=loaner, listing=listing, active = True)
        return agreement
    
    def create_agreement_from_request(self, agreement_request):
        owner = agreement_request.owner
        loaner = agreement_request.loaner
        listing = agreement_request.listing
        agreement =self.create(owner=owner, loaner=loaner, listing=listing, active = True)
        return agreement


#Klasse for å lage avtaler mellom to brukere angående en annonse
class Agreement(models.Model):
    owner = models.ForeignKey(User, verbose_name = "Eier", related_name="agreement_owner", on_delete=models.CASCADE, null=False)
    loaner = models.ForeignKey(User, verbose_name = "Låner", related_name="agreement_loaner", on_delete=models.CASCADE, null=False)
    listing = models.ForeignKey(Listing, related_name = "agreement_listing", on_delete=models.CASCADE)

    start_date = models.DateField(auto_now_add=True, verbose_name ="Startdato")
    end_date = models.DateField(null = True, verbose_name="Sluttdato")
    active = models.BooleanField(null=True)

    objects = AgreementManager()

#Klasse for å lage forespørsel om avtale mellom to brukere angående en annonse
class AgreementRequestManager(models.Manager):
    def create_agreement_request(self, owner, loaner, listing):
        agreementRequest = self.create(owner=owner, loaner=loaner, listing=listing, )
        return agreementRequest


class AgreementRequest(models.Model):
    owner = models.ForeignKey(User, verbose_name = "Eier",  related_name="agreement_req_owner", on_delete=models.CASCADE, null=False)
    loaner = models.ForeignKey(User, verbose_name = "Låner", related_name="agreement_req_loaner", on_delete=models.CASCADE, null=False)
    listing = models.ForeignKey(Listing, related_name = "agreement_req_listing", on_delete=models.CASCADE) 

    objects = AgreementRequestManager()

class UserDefinedList(models.Model):
    owner = models.ForeignKey(User, verbose_name = "Eier",  related_name="list_owner", on_delete=models.CASCADE, null=False)
    listName = models.CharField(max_length=50, verbose_name='navn')
    annonser = models.ManyToManyField(Listing)
