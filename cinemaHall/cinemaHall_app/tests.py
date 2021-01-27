from . import views
from .models import *
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls
import datetime

class AuthenticatedTest(APITestCase):
    client_class = APIClient

    def setUp(self):
        self.username = 'admin'
        self.user = User.objects.create_user(username='admin', email='admin@gmail.com', password='dobrehaselko')
        Token.objects.create(user=self.user)
        super(AuthenticatedTest, self).setUp()

class TransalationTest(AuthenticatedTest):

    def post_translation(self, id_trans, name):
        url = reverse(views.TransalationList.name)
        data = {'id_translation': id_trans, 'name_translation': name}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)

        return response

    def test_post_and_get_translation(self):
        new_id = 1
        new_translation_name = 'Angielski'
        response = self.post_translation(new_id, new_translation_name)

        assert response.status_code == status.HTTP_201_CREATED
        assert Transalation.objects.count() == 1
        assert Transalation.objects.get().name_translation == new_translation_name


    def test_post_delete_translation(self):
        new_id = 1
        new_translation_name = 'Angielski 2'
        response = self.post_translation(new_id, new_translation_name)
        url = urls.reverse(views.TransalationDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_put_update_translation(self):
        new_id = 1
        new_translation_name = 'Angielski'
        new_new_translation_name = 'Niemiecki'
        response = self.post_translation(new_id, new_translation_name)
        url = urls.reverse(views.TransalationDetail.name, None, {response.data['pk']})
        data = {'name_translation': new_new_translation_name}
        patch_response = self.client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name_translation'] == new_new_translation_name

    def test_get_search_translation(self):
        new_id = 1
        new_translation_name = 'Angielski'

        new_id1 = 2
        new_translation_name1 = 'Niemiecki'

        self.post_translation(new_id, new_translation_name)
        self.post_translation(new_id1, new_translation_name1)

        search_data = {'name_translation': new_translation_name}
        url = '{0}?{1}'.format(reverse(views.TransalationList.name), urlencode(search_data))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_translation'] == new_translation_name

    def test_get_filter_translation(self):
        new_id = 1
        new_translation_name = 'Angielski'

        new_id1 = 2
        new_translation_name1 = 'Niemiecki'

        self.post_translation(new_id, new_translation_name)
        self.post_translation(new_id1, new_translation_name1)

        filter_data = {'name_translation': new_translation_name}
        url = '{0}?{1}'.format(reverse(views.TransalationList.name), urlencode(filter_data))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_translation'] == new_translation_name

    def test_get_order_translation(self):
        new_id = 1
        new_translation_name = 'Angielski'

        new_id1 = 2
        new_translation_name1 = 'Niemiecki'

        self.post_translation(new_id, new_translation_name)
        self.post_translation(new_id1, new_translation_name1)

        ordering_address = {'name_translation': new_translation_name}
        url = '{0}?{1}'.format(reverse(views.TransalationList.name), urlencode(ordering_address))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_translation'] == new_translation_name

class TicketOptionsTest(AuthenticatedTest):

    def post_ticket_options(self, id_ticket, name, price, seats):
        url = reverse(views.TicketList.name)
        data = {'id_ticket': id_ticket, 'name_ticket': name, 'price': price, 'number_of_seats': seats}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)

        return response

    def test_post_and_get_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 3
        response = self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)

        assert response.status_code == status.HTTP_201_CREATED
        assert Ticket_options.objects.count() == 1
        assert Ticket_options.objects.get().name_ticket == new_ticket_name
        assert Ticket_options.objects.get().price == new_price
        assert Ticket_options.objects.get().number_of_seats == new_number

    def test_post_delete_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 3

        response = self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)
        url = urls.reverse(views.TicketDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_put_update_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 4

        new_new_price = "250 zł"
        new_new_number = 3
        response = self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)
        url = urls.reverse(views.TicketDetail.name, None, {response.data['pk']})
        data = {'price': new_new_price, 'number_of_seats': new_new_number}
        patch_response = self.client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['price'] == new_new_price
        assert patch_response.data['number_of_seats'] == new_new_number

    def test_get_search_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 4

        new_id1 = 2
        new_ticket_name1 = 'Samotny'
        new_price1 = "20 zł"
        new_number1 = 1

        self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)
        self.post_ticket_options(new_id1, new_ticket_name1, new_price1, new_number1)

        search_data = {'name_ticket': new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.TicketList.name), urlencode(search_data))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_ticket'] == new_ticket_name

    def test_get_filter_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 4

        new_id1 = 2
        new_ticket_name1 = 'Samotny'
        new_price1 = "20 zł"
        new_number1 = 1

        self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)
        self.post_ticket_options(new_id1, new_ticket_name1, new_price1, new_number1)

        filter_data = {'name_ticket': new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.TicketList.name), urlencode(filter_data))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_ticket'] == new_ticket_name

    def test_get_order_ticket_options(self):
        new_id = 1
        new_ticket_name = 'rodzinny'
        new_price = "200 zł"
        new_number = 4

        new_id1 = 2
        new_ticket_name1 = 'Samotny'
        new_price1 = "20 zł"
        new_number1 = 1

        self.post_ticket_options(new_id, new_ticket_name, new_price, new_number)
        self.post_ticket_options(new_id1, new_ticket_name1, new_price1, new_number1)

        ordering_address = {'name_ticket': new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.TicketList.name), urlencode(ordering_address))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name_ticket'] == new_ticket_name