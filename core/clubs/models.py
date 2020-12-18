from django.db import models
from django.urls import reverse


def upload_img(instance, filename):
    return 'university_img/{0}/{1}'.format(instance.title, filename)


def upload_club_img(instance, filename):
    return 'club_img/{0}/{1}'.format(instance.club.title, filename)


def upload_project_img(instance, filename):
    return 'club_img/{0}/{1}/{2}'.format(instance.project.club.title, instance.project.title, filename)


class University(models.Model):
    UNIVERSITIES = (
        ('AIU', 'AlaToo'),
        ('KTU', 'Manas'),
        ('AUCA', 'AUCA'),
        ('INDPT', 'Independent')
    )
    title = models.CharField(max_length=5, choices=UNIVERSITIES)
    image = models.ImageField(upload_to=upload_img)


class Club(models.Model):
    TYPES = (
        ('SR', 'Science and Research'),
        ('CC', 'Creativity and Culture'),
        ('SS', 'Social and Student development'),
        ('EM', 'Entertainment and Media'),
        ('SD', 'Sports and Dancing'),
        ('CH', 'Charity'),
    )
    university = models.ForeignKey(University, models.CASCADE, related_name='univ_club')
    faculty = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=TYPES)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    contacts = models.TextField()

    def get_absolute_url(self):
        return reverse('clubs:club_details', kwargs={'pk': self.pk})


class Project(models.Model):
    club = models.ForeignKey(Club, models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.TextField(default='students')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Gallery(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to=upload_club_img)


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to=upload_project_img)
