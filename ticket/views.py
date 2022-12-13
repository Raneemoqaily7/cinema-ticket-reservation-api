from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie ,Guest,Reservation
from ticket.api.serializers import GuestSerialzer 



# Create your views here.
#Function Based View 
@api_view(["GET" ,"POST"])

def FBV_List (request):
    if request.method =="GET":
        guest  = Guest.objects.all()
        serializer = GuestSerialzer (guest , many =True )
        return Response (serializer.data)


    elif request.method =="POST":
        serializer = GuestSerialzer(data =request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED )
        
        return Response (serializer.data  ,status= status.HTTP_404_NOT_FOUND)
    






        

