from django.urls import path
from .views import home, club_details

app_name = 'clubs'
urlpatterns = [
    path('', home, name='home'),
    path('club_details/<int:pk>/', club_details, name='club_details')
]
