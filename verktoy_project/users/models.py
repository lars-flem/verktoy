from django.db import models
from django.contrib.auth.models import User
from homepage.models import UserDefinedList
from django.core.validators import MaxValueValidator

# Create your models here.

#https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Biografi", null=True)
    tlf = models.PositiveIntegerField(verbose_name="Telefonnummer",validators=[MaxValueValidator(9999999999)], null=True)

    def __str__(self):
        return self.user.username
