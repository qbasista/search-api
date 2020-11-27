from django.test import TestCase
from search_engine.google_api import GoogleService
from googleapiclient.discovery import Resource
from search_api.settings import env

GOOGLE_API_KEY = env('GOOGLE_API_KEY')
GOOGLE_CSE_ID = env('GOOGLE_CSE_ID')

# Create your tests here.

# TODO Mock GoogleService


class GoogleServiceTest(TestCase):

    def setUp(self):
        self.google_api = GoogleService(GOOGLE_API_KEY, GOOGLE_CSE_ID)

    def test_create_google_service(self):

        self.assertEqual(self.google_api.name, 'customsearch')
        self.assertEqual(self.google_api.version, 'v1')
        self.assertEqual(self.google_api.developer_key, GOOGLE_API_KEY)
        self.assertEqual(self.google_api.cse_id, GOOGLE_CSE_ID)
        self.assertIsInstance(self.google_api.service, Resource)
