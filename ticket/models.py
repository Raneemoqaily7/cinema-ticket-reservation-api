from django.db import models

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


    