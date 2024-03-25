from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, EXP


class UserApiTestCase(TestCase):
    # setting up the testcase environment
    def setUp(self):

        # creating two users
        self.u1 = User.objects.create(username="test1")
        self.u2 = User.objects.create(username="test2")
        self.u1.set_password('password')
        self.u2.set_password('password')
        self.u1.save()
        self.u2.save()

        # make use of the APIClient
        self.client = APIClient()

        # login with user 2 and making an exp object
        self.client.login(username="test2", password="password")
        exp = {
            'title': 'test title u2',
            'description': 'test desc2',
            'start_date': '2022-11-10',
            'end_date': '2024-03-22'
        }
        resp = self.client.post('/api/v1/exps/', exp)

    
    # testing the user detail view
    def test_users_details(self):
        resp1 = self.client.get("/api/v1/users/test1")
        resp2 = self.client.get("/api/v1/users/test2")
        self.assertEqual(resp1.json()["username"], self.u1.username)
        self.assertEqual(resp2.json()["username"], self.u2.username)

    
    # testing the creation of an object using post request
    def test_user_post(self):

        self.client.login(username="test1", password="password")
        exp = {
            'title': 'test title u1',
            'description': 'test desc',
            'start_date': '2022-11-10',
            'end_date': '2024-03-22'
        }
        resp = self.client.post('/api/v1/exps/', exp)
        e = EXP.objects.get(user=self.u1, title=exp['title'])
        self.assertEqual(exp['description'], e.description)

    
    # testing the ability to put or patch another users data
    def test_put_permission(self):
        self.client.logout()

        self.client.login(username="test1", password="password")

        e = EXP.objects.get(user=self.u2, id=1)

        new = {"title": "test title u1"}

        resp = self.client.patch("/api/v1/exps/1/", new)

        e = EXP.objects.get(user=self.u2, id=1)

        self.assertNotEqual(new['title'], e.title)


    # test listing objects
    def test_object_list(self):

        resp = self.client.get("/api/v1/exps/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)


    # test the retrieval of an object
    def test_object_retrieve(self):

        resp = self.client.get("/api/v1/exps/1/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['id'], 1)