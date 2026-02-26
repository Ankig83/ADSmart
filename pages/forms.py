from django import forms


class LeadForm(forms.Form):
    source = forms.CharField(required=False)  # блок: ad, contact, stops_calc, etc.
    type = forms.CharField(required=False, max_length=64)  # тип формы: calc_modal, contact, ad
    name = forms.CharField(required=False, max_length=120)
    phone = forms.CharField(required=True, max_length=64)
    business = forms.CharField(required=False, max_length=200)
    company = forms.CharField(required=False, max_length=200)
    interest_format = forms.CharField(required=False, max_length=200)



