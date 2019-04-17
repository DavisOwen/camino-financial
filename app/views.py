from django.views.generic.base import View 
from app.forms import AppForm
from app.models import Loan
from django.shortcuts import render

class FormView(View):

    def get(self, request, *args, **kwargs):
        
        form = AppForm()
        return render(request, "form.html", {"form": form})

    def post(self, request, *args, **kwargs):

        form = AppForm(request.POST)
        loan = Loan()
        if form.is_valid():
            loan = Loan()
            data = form.cleaned_data
            loan.name = data["name"]
            loan.amount = data["amount"]
            loan.business = data["business"]
            loan.years = data["years"]
            loan.save()
            if data["amount"] > 50000 and data["years"] < 1:
                return render(request, "denied.html")
            elif data["amount"] < 50000 and data["years"] >= 1:
                return render(request, "approved.html")
            else:
                return render(request, "process.html")
        return render(request, "form.html", {"form": form})
