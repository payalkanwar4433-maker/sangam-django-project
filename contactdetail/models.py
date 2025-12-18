from django.db import models

# Create your models here.
class Contactform(models.Model):
    username=models.CharField(max_length=500)
    usermail=models.CharField(max_length=250)

