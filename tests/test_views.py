from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    #set up test account 
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        #authenticate the test user
        self.client.force_login(user=self.user)

        #crete test post
        self.post = Menu.objects.create(title="Pizza", price=10.50, inventory=20)

    def test_get_menu_queryset(self):
        url = reverse('menu')
        resoponse = self.client.get(url)
        self.assertEqual(resoponse.status_code, status.HTTP_200_OK)


         
  