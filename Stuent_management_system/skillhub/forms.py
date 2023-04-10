from django import forms
from .models import Person



class Personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'dept','year','role','phone']


class PersonSearchform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','role']
        
