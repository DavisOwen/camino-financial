from django.views.generic.base import View 
from caminofinancial.forms import AppForm
from django.shortcuts import render

class FormView(View):

    def get(self, request, *args, **kwargs):
        
        form = AppForm()
        return render(request, "form.html", {"form": form})

    def post(self, request, *args, **kwargs):

        form = AppForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data["amount"] > 50000 and data["years"] < 1:
                return render(request, "denied.html")
            elif data["amount"] < 50000 and data["years"] >= 1:
                return render(request, "approved.html")
            else:
                return render(request, "process.html")
        return render(request, "form.html", {"form": form})
