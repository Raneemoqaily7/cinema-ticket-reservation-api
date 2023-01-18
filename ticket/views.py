
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 
from .models import Movie ,Guest,Reservation ,Review
from ticket.api.serializers import GuestSerialzer ,MovieSerializer ,ReservationSerialzer,ReviewSerilaizer
from ticket.api.permissions import  IsOwnerOrReadOnly ,OwnerOnly 
from django.http import HttpResponse

from rest_framework.decorators import authentication_classes ,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





#search by id and number (CBV)
# class GuestListView(generics.ListAPIView):
#     queryset = Guest.objects.all()
#     serializer_class = GuestSerialzer
#     authentication_classes=[TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['id', '=number']

# Create your views here.
#Function Based View


# search on movie and guset(FBV)
@api_view(["GET" ])
def find_movie(request):
    movie = Movie.objects.filter(
        titel =request.data['titel']
       
    )
    serializer = MovieSerializer (movie ,many=True )
    return Response (serializer.data)

@api_view(["GET" ])
def find_guest(request):
    guest = Guest.objects.filter(
        name =request.data['name']
       
    )
    serializer = GuestSerialzer (guest ,many=True )
    return Response (serializer.data)



@api_view(["GET" ,"POST"])
# @permission_classes((IsOwnerOrReadOnly, ))


def FBV_List (request):


    
    if request.method =="GET":
        guest  = Guest.objects.all()
        serializer = GuestSerialzer (guest ,many=True)
     
        

        return Response (serializer.data ,status = status.HTTP_200_OK)



    
    

    elif request.method =="POST":
        serializer = GuestSerialzer(data =request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED )
        
        return Response (serializer.errors ,status= status.HTTP_404_NOT_FOUND)
    

@api_view(["GET" ,"PUT" ,"DELETE"])

def FBV_id (request , id): #get one oobject by name or (id) 
    guest = Guest.objects.get (id = id)
    if request.method == "GET" :
        
        serializer = GuestSerialzer (guest )
        return Response (serializer.data)
    

    if request.method == "PUT":
        serializer = GuestSerialzer(guest ,data = request.data  )
        response ={}
        if serializer.is_valid ():
            serializer.save()
            response=serializer.data
            return Response (data=response)
        return Response ( serializer.errors ,status=status.HTTP_400_BAD_REQUEST )
        
    if request.method == "DELETE":
        operation = guest.delete()
        if operation :
            data = "delete successful"
        else :
            data = "delete failur"
        return Response (data = data ,status = status.HTTP_204_NO_CONTENT)

    
    
        



@api_view(["POST"])
    
def new_reversation (request):
    if request.method == "POST":
      movie = Movie.objects.get(
        titel =request.data['titel'],
        hall=request.data["hall"]
      
       
    )
      
      
      guest = Guest()
      guest.name = request.data["name"]
      guest.number= request.data["number"]
      guest.save()

      reservtion = Reservation()
      reservtion.guest = guest

      reservtion.movie = movie
      reservtion.save()

      data ={}
      serializer = ReservationSerialzer(data=request.data)
      if serializer.is_valid():
          serializer.save()     
          data  =serializer.data
          return Response (data =data )
      return Response (serializer.errors)


      
            # return Response(serializer.data , status = status.HTTP_200_OK)
    #   return Response(serializer.data , status = status.HTTP_404_NOT_FOUND)
        

@api_view(["GET" ])



def FBV_reserv (request):
    

    
    if request.method =="GET":
        reservation = Reservation.objects.all()
        guest = Guest()
        movie=Movie()
        
        serializer = ReservationSerialzer (reservation , many =True )
     
        

        return Response (serializer.data ,status = status.HTTP_200_OK)





@api_view (["GET" ,"POST" ,"PUT" ,"DELETE"])
@authentication_classes(( TokenAuthentication,))
@permission_classes((IsOwnerOrReadOnly, ))

def reviews (request , id ):
    if request.method == "GET":
        review =Review.objects.all() 
        serializer = ReviewSerilaizer (review ,many=True)
        return Response(serializer.data)

    elif request.method =="POST":
        serializer = ReviewSerilaizer (data =request.data)
        if serializer.is_valid ():
            serializer.save()

            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.data  ,status= status.HTTP_404_NOT_FOUND)
        
    
    elif request.method == "PUT":
        review = Review.objects.get (id = id )
        serializer =ReviewSerilaizer(review ,data = request.data  )
        if serializer.is_valid ():
            data = {}
            serializer.save()
            data = serializer.data
            return Response (data = data)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        

   