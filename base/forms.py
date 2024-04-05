from django import forms

from base.models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["tax_id", "name", "annual_revenue"]
