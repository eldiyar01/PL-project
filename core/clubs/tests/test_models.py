import datetime
from django.test import TestCase

from clubs.models import University, Club, Project


class UniversityModelTestCase(TestCase):
    def setUp(self):
        University.objects.create(abbreviation="AIU", title="Ala-Too", image='core/media/university_img/AIU/alatoo.png')

    def test_university(self):
        univ = University.objects.get(title="Ala-Too")
        self.assertEqual(univ.title, "Ala-Too")
        self.assertEqual(univ.abbreviation, "AIU")
        self.assertEqual(univ.image, "core/media/university_img/AIU/alatoo.png")


class ClubModelTestCase(TestCase):

    def setUp(self):
        univ = University.objects.create(abbreviation="AIU", title="Ala-Too")
        Club.objects.create(university=univ, faculty='Computer Science', type="SR", title="WEB", date="2020-12-01",
                            description="description", contacts="call me")

    def test_club(self):
        club = Club.objects.get(title="WEB")
        self.assertEqual(club.faculty, "Computer Science")
        self.assertEqual(club.type, "SR")
        self.assertEqual(club.title, "WEB")
        self.assertEqual(club.date, datetime.date(2020, 12, 1))
        self.assertEqual(club.description, "description")
        self.assertEqual(club.contacts, "call me")

    def test_get_absolute_url(self):
        club = Club.objects.get(id=1)
        self.assertEqual(club.get_absolute_url(), '/club_details/1/')


class ProjectModelTestCase(TestCase):
    def setUp(self):
        univ = University.objects.create(abbreviation="AIU", title="Ala-Too")
        club = Club.objects.create(university=univ, faculty='Computer Science', type="SR", title="WEB",
                                   date="2020-12-01", description="description", contacts="call me")
        Project.objects.create(club=club, title="App", description="description", author="Eldiiar",
                               start_date="2020-12-01", end_date="2021-12-01")

    def test_project(self):
        app = Project.objects.get(title="App")
        self.assertEqual(app.title, "App")
        self.assertEqual(app.description, "description")
        self.assertEqual(app.author, "Eldiiar")
        self.assertEqual(app.start_date, datetime.date(2020, 12, 1))
        self.assertEqual(app.end_date, datetime.date(2021, 12, 1))

    def test_get_absolute_url(self):
        project = Project.objects.get(id=1)
        self.assertEqual(project.get_absolute_url(), '/project_details/1/')
