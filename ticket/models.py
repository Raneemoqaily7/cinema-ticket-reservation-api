from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.conf import settings 
from rest_framework.authtoken.models import Token
# Create your models here.

class Movie (models.Model):
    titel = models.CharField(max_length= 30)
    hall = models.CharField(max_length=25)
    date=models.DateField()


    def __str__(self):
        return self.titel

class Guest (models.Model):
    name = models.CharField (max_length= 30)
    number =models.CharField (max_length= 10)
    

    def __str__(self):
        return self.name


class Reservation (models.Model):
    guest =models.ForeignKey(Guest  ,related_name="reservation" , on_delete=models.PROTECT )
    movie = models.ForeignKey(Movie , on_delete=models.PROTECT )


    def __str__(self):
        return str (self.guest)
    

class Review(models.Model):
    title = models.CharField(max_length=20)
    reviewer = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE )
    time_created =models.TimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return str(self.reviewer)
    

@receiver(post_save , sender =settings.AUTH_USER_MODEL)
def create_token (created ,sender , instance   ,**kwargs):
    if created:
        Token.objects.create(user =instance)

    


    