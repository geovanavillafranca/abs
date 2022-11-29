from django.test import TestCase
from ..models.client import Client


class TestClientModel(TestCase):
    def setUp(self):
        # self.client = {
        #     'name': 'Client', 
        #     'company_name': 'Company name',
        #     'phone_number': '11 99999 9999',
        #     'address': 'Rua test, 22',
        #     'zone': 'Zona norte'
        #     }
        self.data = Client.objects.create(
            name='Client', 
            company_name='Company name',
            phone_number='11 99999 9999',
            address='Rua test, 22',
            zone='Zona norte'
            )

    def test_check_created_client(self):
        self.assertEqual(self.data.name, Client.objects.get(id=1).name)



