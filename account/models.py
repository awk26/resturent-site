from django.db import models

from django.db import models

from django import forms

class LoginForm(forms.Form):
   
    uname=forms.CharField(label="username",widget=forms.TextInput(attrs={'autofocus':'true', 'class':'form-control' }))
    pswd=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'autofocus':'true', 'class':'form-control' }))

