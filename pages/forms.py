from django import forms


class LeadForm(forms.Form):
    source = forms.CharField(required=False)  # "ad" | "contact"
    name = forms.CharField(required=False, max_length=120)
    phone = forms.CharField(required=True, max_length=64)
    business = forms.CharField(required=False, max_length=200)
    company = forms.CharField(required=False, max_length=200)
    interest_format = forms.CharField(required=False, max_length=200)



