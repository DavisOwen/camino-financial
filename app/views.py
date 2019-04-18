from app.models import Loan
from django.shortcuts import render
from app.serializers import LoanSerializer
from rest_framework import generics, mixins

class LoanCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def post(self, request, *args, **kwargs):
        
        query = request.POST
        self.create(request, *args, **kwargs)
        if int(query["amount"]) > 50000 and int(query["years"]) < 1:
            return render(request, "denied.html")
        elif int(query["amount"]) < 50000 and int(query["years"]) >= 1:
            return render(request, "approved.html")
        return render(request, "process.html")
