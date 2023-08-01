from django import forms
from .models import *


class CartItem(forms.ModelForm):
    class Meta:
        model=Cart
        fields="__all__"