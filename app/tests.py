from django.test import TestCase
from app.models import Loan
from app.forms import AppForm

class CreateLoan(TestCase):

    def create(self):

        self.loan = Loan.objects.create(name = "Name", amount = 10000, business = "food_truck", years = 1)

class FormTest(TestCase):

    def test_form_valid(self):

        form = AppForm(data = {"name":"Name", "amount":10000, "business" : "food_truck", "years" : 1})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):

        form = AppForm(data = {"name":"", "amount":10, "business":"foo", "years": 1000})
        self.assertFalse(form.is_valid())
