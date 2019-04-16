from django.forms import Form, CharField, IntegerField, ChoiceField

class AppForm(Form):

    name = CharField(label="Name")
    amount = IntegerField(label="Amount Required")
    business = ChoiceField(label="Business Type", choices=[("food_truck", "Food Truck"), ("construction", "Construction"), ("others", "Others")])
    years = IntegerField(label="Years in Business")
