from django import forms
from blog.models import Restaurant

class RestForm(forms.ModelForm):  # ModelForm -> 
    class Meta:
        model = Restaurant
        fields = '__all__'