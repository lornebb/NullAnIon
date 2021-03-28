from django.test import TestCase
from .forms import OrderForm


class OrderTest(TestCase):
    def setUp(self):
        OrderForm.objects.create(
            full_name="Testy McTestFace",
            email="testy@test.face",
            phone_number="99999999",
        )

    def test_review_content_is_required(self):
        form = OrderForm({'review_content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'], 'This field is required.')

    def order_works(self):
        """Order forms that are valid work"""
        form = OrderForm()
        self.assertNotEquals(form.Meta.exclude, ['full_name', 'email'])
