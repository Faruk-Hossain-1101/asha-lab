from django import forms
from lab.models.customer import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'gender', 'address', 'id_type', 'id_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control phone'}),
            'gender': forms.Select(attrs={'class': 'form-control phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'id_type': forms.Select(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control phone'}),
        }
