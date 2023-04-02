from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        queryset = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        serializer = MenuSerializer(queryset)
        self.assertEqual(serializer.data['Title'], "IceCream")