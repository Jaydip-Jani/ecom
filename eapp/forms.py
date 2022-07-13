from django import forms
from .models import *


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreateSubcategory(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
