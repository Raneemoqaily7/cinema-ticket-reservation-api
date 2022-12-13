from django.urls import path 
from ticket import views

urlpatterns = [
    path('guest-list/', views.FBV_List ),

   
]
