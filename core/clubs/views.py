from django.shortcuts import render
from .models import University, Club, Project


def home(request):
    universities = University.objects.all()
    clubs = Club.objects.all()
    return render(request, 'clubs/home.html', {'universities': universities,
                                               'clubs': clubs})


def club_details(request, pk):
    club = Club.objects.get(id=pk)
    return render(request, 'clubs/details.html', {'club': club})


def project_details(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'clubs/project.html', {'project': project})
