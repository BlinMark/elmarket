from django.test import TestCase
from django.test import Client
from orders.forms import *
from blog.models import Product, Category
from .models import *
from cart.cart import Cart
import unittest


class OrderUpdate:
    def __init__(self):
        self.apple = Product.objects.create(name="apple", slug="apple", price="4")
        self.cart = Cart.session.create(quantity=1)

    # Valid
    def updateQuantity(self):
        self.assertEqual(self.cart.add(quantity=2))


class CategoryTest(TestCase):
    def __init__(self):
        self.fruit = Category.objects.create(name="fruit", slug="fruit")

    # Valid
    def save_category(self):
        self.assertEqual(self.fruit.save(), data={"name": "fruit", "slug": "fruit"})


class ProuctTest(TestCase):
    def __init__(self):
        self.apple = Product.objects.create(name="apple", slug="apple", price="4")

    # Valid
    def save_test(self):
        self.assertEqual(self.apple.save(), data={"name": "apple", "slug": "apple", "price": "4"})


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(title="MyPost")
        self.assertEquals(str(post), post.title)


class SetUp(TestCase):
    def setUp(self):
        self.order = User.objects.create(first_name="Mark", phone="80296400621", email="email@email.com",
                                         street="Street", home="5", flat="19")

        self.user = User.objects.create_user('admin', 'admin@gmail.com', 'admin')


class UserFormTest(TestCase):
    # Valid Form Data
    def test_UserForm_valid(self):
        form = OrderCreateForm(data={'first_name': "Mark", 'phone': "80296400621", 'email': "email@email.com",
                                     'street': "Street", 'home': "5", 'flat': "19"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = OrderCreateForm(data={'first_name': "X", 'phone': "1", 'email': "2",
                                     'street': "3", 'home': "4", 'flat': "5"})
        self.assertFalse(form.is_valid())


class LoginTest(TestCase):
    # Valid login
    def login_test_valid(self):
        self.client.login(username="admin", password="admin")
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.context['email'], 'admin@gmail.com')

    # Invalid login
    def login_test_invalid(self):
        self.client.login(username="admin", password="notadmin")
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.context['email'], 'admin@gmail.com')
