from django import forms


class SityForm(forms.Form):
    # your_sity = forms.CharField(label='Enter sity', max_length=100)
    # class Meta:
    #     fields = ('your_sity',)
    #     widgets = {
    #         'your_sity': forms.TextInput(attrs={'class': 'form-control'})
    #     }
    your_sity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control me-2', 'type': 'search', 'placeholder': 'Sity', 'aria-label': 'Search', 'autocomplete': 'off'}), max_length=100, label='')
