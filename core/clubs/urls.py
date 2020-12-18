from django.urls import path
from .views import home, club_details

app_name = 'clubs'
urlpatterns = [
    path('', home, name='home'),
    path('details/<int:pk>/', club_details, 'club_details')
]
