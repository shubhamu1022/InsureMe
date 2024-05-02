from django import forms

class InsuranceForm(forms.Form):
    CATEGORY_CHOICES = [
        ('Whole Life', 'Whole Life'),
        ('Critical Illness', 'Critical Illness'),
        ('Savings', 'Savings')
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    max_premium = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text="Enter the maximum monthly premium you are willing to pay.")
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_age'}))

    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['style'] = 'display: none;'  # Initially hide the age field
