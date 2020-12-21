import datetime
from django.test import TestCase

from clubs.models import University, Club, Project


class PagesTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_features(self):
        response = self.client.get('/features/')
        self.assertEquals(response.status_code, 200)

    def test_team(self):
        response = self.client.get('/team/')
        self.assertEquals(response.status_code, 200)


class ClubViewTestCase(TestCase):

    def setUp(self):
        univ = University.objects.create(abbreviation="AIU", title="Ala-Too")
        Club.objects.create(university=univ, faculty='Computer Science', type="SR", title="WEB", date="2020-12-01",
                            description="description", contacts="call me")

    def test_club_details(self):
        response = self.client.get('/club_details/1/')
        self.assertEquals(response.status_code, 200)


class ProjectViewTestCase(TestCase):

    def setUp(self):
        univ = University.objects.create(abbreviation="AIU", title="Ala-Too")
        club = Club.objects.create(university=univ, faculty='Computer Science', type="SR", title="WEB",
                                   date="2020-12-01", description="description", contacts="call me")
        Project.objects.create(club=club, title="App", description="description", author="Eldiiar",
                               start_date="2020-12-01", end_date="2021-12-01")

    def test_project_club_details(self):
        response = self.client.get('/project_details/1/')
        self.assertEquals(response.status_code, 200)


class SearcherViewTestCase(TestCase):

    def setUp(self):
        univ = University.objects.create(abbreviation="AIU", title="Ala-Too")
        club = Club.objects.create(university=univ, faculty='Computer Science', type="SR", title="WEB",
                                   date="2020-12-01", description="description", contacts="call me")
        Project.objects.create(club=club, title="App", description="description", author="Eldiiar",
                               start_date="2020-12-01", end_date="2021-12-01")

    def test_search(self):
        inp = "Ala"
        u_results = University.objects.filter(title__icontains=inp)
        self.assertEqual(u_results.first().title, "Ala-Too")
        inp = "We"
        c_results = Club.objects.filter(title__icontains=inp)
        self.assertEqual(c_results.first().title, "WEB")

    def test_searcher(self):
        response = self.client.get('/search/')
        self.assertEquals(response.status_code, 200)
