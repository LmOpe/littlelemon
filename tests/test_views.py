from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def test_getall(self):
        item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        item2 = Menu.objects.create(Title="Cake", Price=100, Inventory=40)
        items = Menu.objects.all()
        self.assertEqual(len(items), 2)