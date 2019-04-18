from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app.models import Loan

class LoanAPITestCase(APITestCase):

    def test_create_loan(self):

        loan = Loan.objects.create(name = "Name",
                                    amount = 10000,
                                    business = "food_truck",
                                    years = 1)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.get().name, "Name")
        self.assertEqual(Loan.objects.get().amount, 10000)
        self.assertEqual(Loan.objects.get().business, "food_truck")
        self.assertEqual(Loan.objects.get().years, 1)

    def test_get_status(self):

        data = {}
        url = reverse("loan-create")
        response = self.client.get(url, data, format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_status(self):

        data = {"name" : "Name", "amount" : 10, "business" : "construction", "years" : 2}
        url = reverse("loan-create")
        response = self.client.post(url, data, format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
