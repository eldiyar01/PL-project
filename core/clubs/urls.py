from django.urls import path
from .views import home, club_details, project_details, searcher

app_name = 'clubs'
urlpatterns = [
    path('', home, name='home'),
    path('club_details/<int:pk>/', club_details, name='club_details'),
    path('project_details/<int:pk>/', project_details, name='project_details'),
    path('search/', searcher, name='searcher'),
]
