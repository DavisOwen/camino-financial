from rest_framework import serializers

from app.models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            'pk',
            'name',
            'amount',
            'business',
            'years',
        ]
