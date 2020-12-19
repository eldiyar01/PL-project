from django.shortcuts import render, redirect

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


def searcher(request):
    inp = request.GET.get('search')
    rad = request.GET.get('search_by')
    u_results = None
    c_results = None
    if inp is str():
        return redirect('clubs:home')
    if rad == 'univ':
        u_results = University.objects.filter(title__icontains=inp)
    elif rad == 'club':
        c_results = Club.objects.filter(title__icontains=inp)
    return render(request, 'clubs/search.html', {'input': inp, 'universities': u_results, 'clubs': c_results})


def features(request):
    return render(request, 'features/soon.html')


def team(requeset):
    return render(requeset, 'about/team.html')
