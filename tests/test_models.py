from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(title="IceCream", price=3.5, inventory=100)
        self.assertEqual(str(item), "IceCream: 3.5")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Salad", price=6)
        self.assertTrue(item.inventory, 10)
    
