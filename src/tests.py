from django.test import TestCase
import requests

# Create your tests here.
from django.urls import reverse
from src.models import NetworkMobile, Network
from src.utils import convert_lambert93_to_wgs84, create_networks




class ViewsTestCase(TestCase):
    def setUp(self):
        create_networks()
        self.external_url = "https://api-adresse.data.gouv.fr/search/?q=8+rue+lebon"
        self.uri = "http://127.0.0.1:8000/api/"
        self.address = "72 Avenue de Wagram"
        self.zipcode = "75017"
        self.network = Network.objects.get(code=20801)
        self.network_mobile = NetworkMobile.objects.create(
            operator=self.network, x=648743, y=6864116, g2=False, g3=True, g4=True,
            coordinate_x=48.88, coordinate_y=2.3)
        self.network2 = Network.objects.get(code=20810)
        self.network_mobile2 = NetworkMobile.objects.create(
            operator=self.network2, x=648743, y=6854116, g2=True, g3=True, g4=True,
            coordinate_x=48.88, coordinate_y=2.29)

    def test_check_coordinates(self):
        resp = convert_lambert93_to_wgs84(self.network_mobile.x, self.network_mobile.y)
        self.assertEqual(round(resp['coordinate_x'], 2),
                         self.network_mobile.coordinate_x)
        self.assertEqual(round(resp['coordinate_y'], 2), self.network_mobile.coordinate_y)

    def test_external_api_adresse(self):
        response = requests.get(self.external_url)
        self.assertEqual(response.status_code, 200)

    def test_network_coverage(self):
        url = reverse('networks')
        response = self.client.get(url, {'address': self.address, 'zipcode': self.zipcode})
        self.assertEqual(response.status_code, 200)
        self.assertIn('2G', str(response.json()))
