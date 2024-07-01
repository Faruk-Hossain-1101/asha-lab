from django import forms
from lab.models.agent import Doctor
from lab.models.lab import Discount

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'expaties', 'degree', 'address', 'discount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'expaties': forms.TextInput(attrs={'class': 'form-control phone'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'discount': forms.Select(attrs={'class': 'form-control phone'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['discount'].queryset = Discount.objects.order_by('-id').all()
