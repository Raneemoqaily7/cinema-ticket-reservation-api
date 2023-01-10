from django.urls import path 
from ticket import views
from django.urls import path ,include

# from .views import GuestListView

urlpatterns = [
    path('guest-list/', views.FBV_List ),
    path('guest-detail/<str:name>/', views.FBV_id),
    path('movie-find/', views.find_movie),
    path('guest-find/', views.find_guest),
    path('new-reserv/', views.new_reversation),
    path('reserv/', views.FBV_reserv),

    # path ('guest' ,GuestListView.as_view() )   #test

   
]
 