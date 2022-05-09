from django import forms
from.models import Laptop
#from django.core import validators


ram=[
    ('8gb', '8GB'),
    ('16gb', '16GB'),
    ('32gb', '32GB'),
    ('64gb', '64GB')
]

seller=[
    ('lotus', 'Lotus'),
    ('Reliance', 'Reliance'),
    ('city collection', 'City collection'),
    ('trends', 'Trends')
]
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'laptop_id': 'LAPTOP ID',
            'name': 'NAME',
            'model': 'MODEL',
            'brand': 'BRAND',
            'ram': 'RAM',
            'price': 'PRICE',
            'date': 'DATE',
            'phoneno': 'PHONE NO',
            'seller': 'SELLER',
            'address': 'ADDRESS'
        }
        widgets = {
            'laptop_id':forms.NumberInput(attrs={'placeholder':'Enter laptop Id'}),
            'name':forms.TextInput(attrs={'placeholder':'Enter name' }),
            'model':forms.TextInput(attrs={'placeholder':'Enter model name'}),
            'ram':forms.RadioSelect(choices=ram),
            'price':forms.NumberInput(attrs={'palceholder':'Enter laptop Price'}),
            'date':forms.DateInput(attrs={'type':'date'}),
            'seller':forms.CheckboxSelectMultiple(choices=seller),
            'address':forms.Textarea(attrs={'placeholder':'Enter shop address', 'rows':3})

        }

    def clean_name(self):
        value = self.cleaned_data['name']
        if value.istitle() !=True:
            raise forms.ValidationError('frist character is capital!!')
        return value
