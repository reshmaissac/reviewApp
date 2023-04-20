from django import forms
from .models import *
from django.forms import DateInput

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','brand','category','cost','release_date','description','photo')
		widgets = {
            'release_date': DateInput(attrs={'type': 'date'})
        }


# class ReviewForm(forms.ModelForm):  
#     class Meta:  
#         model = Review  
#         fields = ('rating','comment')  