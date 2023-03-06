from django.test import TestCase
from django.template import Context, Template
from .models import Menu, MenuItem


class MenuTemplateTagTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(slug='TestMenu')
        cls.item_1 = MenuItem.objects.create(slug='i1', menu=cls.menu)
        cls.item_1_1 = MenuItem.objects.create(slug='i11', parent=cls.item_1)
        cls.item_2 = MenuItem.objects.create(slug='i2', menu=cls.menu)
        cls.item_2_1 = MenuItem.objects.create(slug='i21', parent=cls.item_2)


    def test_get_menu_without_inline(self):
        wsgi_request = self.client.get(f"/TestMenu/", {}).wsgi_request

        out = Template(
            "{% load menu %}"
            "{% draw_menu 'TestMenu' %}"
        ).render(Context({'request': wsgi_request}))

        self.assertEqual(out, '<div><a href="/TestMenu">TestMenu</a><ul></ul></div>')


    def test_get_menu_with_inline(self):
        wsgi_request = self.client.get(f"/TestMenu-i1-i11", {}).wsgi_request

        out = Template(
            "{% load menu %}"
            "{% draw_menu 'TestMenu' %}"
        ).render(Context({'request': wsgi_request}))

    
        self.assertEqual(out, '<div><a href="/TestMenu">TestMenu</a><ul><li><a href="TestMenu-i1">i1</a><ul><li><a href="TestMenu-i1-i11">i11</a><ul></ul></li></ul></li><li><a href="TestMenu-i2">i2</a><ul></ul></li></ul></div>')