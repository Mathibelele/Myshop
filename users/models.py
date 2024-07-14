from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField()