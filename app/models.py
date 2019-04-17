from django.db.models import Model, CharField, IntegerField

class Loan(Model):

    name = CharField(max_length=100)
    amount = IntegerField()
    business = CharField(max_length=100)
    years = IntegerField()
