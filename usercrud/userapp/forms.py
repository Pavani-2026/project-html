from django import forms
from userapp.models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['name','email','age','address']