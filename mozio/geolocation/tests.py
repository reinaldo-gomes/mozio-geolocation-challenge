from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from geolocation.models import Provider, ServiceArea
import json


class GeolocationTests(APITestCase):
    def test_list_providers(self):
        url = reverse('provider-list')
        provider = Provider(
            name='provider01',
            email='email@email.com',
            phone_number='1234',
            language='ENGLISH',
            currency='USD',
        )
        provider.save()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(f'{url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_provider(self):
        url = reverse('provider-list')
        data = {
            'name': 'provider01',
            'email': 'provider01@email.com',
            'phone_number': '1234',
            'language': 'ENGLISH',
            'currency': 'USD'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)

    def test_list_service_areas(self):
        provider = Provider(
            name='provider01',
            email='provider01@email.com',
            phone_number='1234',
            language='ENGLISH',
            currency='USD'
        )
        provider.save()
        area = ServiceArea(
            provider=provider,
            name='area01',
            price=1000,
            geolocation={}
        )
        area.save()

        url = reverse('servicearea-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(f'{url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_service_area(self):
        url = reverse('servicearea-list')
        provider = Provider(
            name='provider01',
            email='provider01@email.com',
            phone_number='1234',
            language='ENGLISH',
            currency='USD'
        )
        provider.save()

        response = self.client.get(f'{reverse("provider-list")}1/')
        data = {
            'provider': response.json()['url'],
            'name': 'area01',
            'price': 1000,
            'geolocation': {}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)

    def test_overlapping_areas(self):
        provider = Provider(
            name='provider01',
            email='provider01@email.com',
            phone_number='1234',
            language='ENGLISH',
            currency='USD'
        )
        provider.save()
        area = ServiceArea(
            provider=provider,
            name='area01',
            price=1000,
            geolocation={
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[10, 20], [12, 20], [12, 22], [10, 22]]
                }
            }
        )
        area.save()
        area = ServiceArea(
            provider=provider,
            name='area02',
            price=2000,
            geolocation={
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[22, 33], [23, 33], [23, 34], [22, 34]]
                }
            }
        )
        area.save()

        expected_data = [{
            'provider': 'provider01', 'name': 'area01', 'price': 1000.0, 'geolocation': {
                'geometry': {'type': 'Polygon', 'coordinates': [[10, 20], [12, 20], [12, 22], [10, 22]]}
            }
        }]
        url = reverse('overlapping_areas')

        response = self.client.get(url, {'lat': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {'lng': 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {'lat': 11, 'lng': 21})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(json.dumps(expected_data), response.json())
