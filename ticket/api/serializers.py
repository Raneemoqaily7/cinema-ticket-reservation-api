from rest_framework import serializers
from ticket.models import Movie , Guest ,Reservation ,Review


class MovieSerializer (serializers.ModelSerializer):

    class Meta :
        model =  Movie
        fields ='__all__'

class ReservationSerialzer(serializers.ModelSerializer):

    class Meta :
        model =Reservation
        fields = '__all__'

class  GuestSerialzer(serializers.ModelSerializer):

    class Meta :
        model =Guest
        fields = ["id" , "name" , "number" , "reservation"]


class ReviewSerilaizer (serializers.ModelSerializer):
    class Meta :
        model= Review
        fields = '__all__'



