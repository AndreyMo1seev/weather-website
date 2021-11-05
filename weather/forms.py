from django import forms


class SityForm(forms.Form):
    your_sity = forms.CharField(label='Enter sity', max_length=100)