from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CountryTestCase(APITestCase):
    profile_list_url = reverse('country_list_create')
    profile_data = {'name': 'Ecuador', 'iso_code': 'EC', }
    profile_data_update = {'name': 'Panama', 'iso_code': 'PA', }

    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        # obtain a json web token for the newly created user
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_country_create(self):
        response = self.client.post(self.profile_list_url, data=self.profile_data)
        status.is_success(response.status_code)

    def test_country_list(self):
        response = self.client.get(self.profile_list_url)
        status.is_success(response.status_code)

    def test_country_update(self):
        response = self.client.put(reverse('country_detail', kwargs={'pk': 1}), data=self.profile_data_update)
        status.is_success(response.status_code)

    def test_country_details(self):
        response = self.client.get(reverse('country_detail', kwargs={'pk': 1}))
        status.is_success(response.status_code)

    def test_country_delete(self):
        response = self.client.delete(reverse('country_detail', kwargs={'pk': 1}))
        status.is_success(response.status_code)
