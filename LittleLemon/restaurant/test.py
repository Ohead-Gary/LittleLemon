from django.test import TestCase
from .models import Menu
from .views import MenuItemView
from .serializers import MenuSerializer
from django.urls import reverse


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):

        Menu.objects.create(Title='IceCream1', Price=80, Inventory=100)
        Menu.objects.create(Title='IceCream2', Price=180, Inventory=100)
        Menu.objects.create(Title='IceCream3', Price=280, Inventory=100)
    
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)