from django.urls import path
from .views import home

app_name = 'universities'
urlpatterns = [
    path('', home, name='home'),
]
